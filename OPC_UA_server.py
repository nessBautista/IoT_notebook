import asyncio
import random
from asyncua import ua, Server
from asyncua.common.methods import uamethod
import logging

import MockPLC
from MockPLC import MockPLC

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('asyncua')

async def main():
    # setup our server
    server = Server()
    await server.init()
    server.set_endpoint('opc.tcp://0.0.0.0:4840/opcua/')    # If available, IP of Raspberry pi should be set here
    server.set_server_name("DevNet OPC-UA Test Server")
    # setup our own namespace, not really necessary but should as spec
    idx = await server.register_namespace("PLC_namespace")

    # populating our address space
    obj_vplc = await server.nodes.objects.add_object(idx, 'vPLC')

    # Add our sensor data
    plc = MockPLC()
    sensors_data = plc.sensor_output()

    # Add data from timestamp and the first 3 sensors
    var_sensor00 = await obj_vplc.add_variable(idx, sensors_data.columns[2], 0.0) #sensor_00
    var_sensor01 = await obj_vplc.add_variable(idx, sensors_data.columns[3], 0.0) #sensor_01
    var_sensor02 = await obj_vplc.add_variable(idx, sensors_data.columns[4], 0.0) #sensor_02

    _logger.info("starting server...")

    async with server:
        # run forever every 5 secs
        for index, row in sensors_data.iterrows():
            print("Data sent from PLC to server:")
            print(row['sensor_00'])
            print(row['sensor_01'])
            print(row['sensor_02'])
            await var_sensor00.write_value(row['sensor_00'])
            await var_sensor01.write_value(row['sensor_01'])
            await var_sensor02.write_value(row['sensor_02'])
            await asyncio.sleep(3)

if __name__ == '__main__':
    asyncio.run(main())