import asyncio
import logging
import paho.mqtt.client as mqtt
import json
from asyncua import Client, Node, ua
import os

logger = logging.getLogger('asyncua')
logging.disable(logging.WARNING)


data_variables = ["sensor_00", "sensor_01","sensor_02"]
iot_hub = "demo.thingsboard.io"
port = 1883
username =  os.environ['username']
password = ""
topic = "v1/devices/me/telemetry"

iot_hub_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
iot_hub_client.username_pw_set(username, password)
iot_hub_client.connect(iot_hub, port, port)
print("connected to IoT Hub")



async def dict_format(keys, values):
  return dict(zip(keys, values))

async def main():
    while True:
        url = "opc.tcp://0.0.0.0:4840/opcua/"
        async with Client(url=url) as client:
            data_list = []
            namespace = "PLC_namespace"
            idx = await client.get_namespace_index(namespace)
            for i in range(len(data_variables)):
                myvar = await client.nodes.root.get_child(["0:Objects", "{}:vPLC".format(idx), "{}:{}".format(idx,data_variables[i])])
                val = await myvar.get_value()
                data_list.append(val)
            data = await dict_format(data_variables,data_list)
            print("Data received from server:")
            print(data)

            # send data to things board: MQTT
            data_board_things = json.dumps(data)
            iot_hub_client.publish(topic, data_board_things, 0)
            await asyncio.sleep(3)

if __name__ == '__main__':
    asyncio.run(main())