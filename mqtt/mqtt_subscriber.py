import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectando al broker")
        global Connected
        Connected = True
    else:
        print("Error al conectar")
    return

def on_message(client, userdata, message):
    print("mensaje recibido: {} - {}".format(message.topic, message.payload))
    return

broker_address = "broker.hivemq.com"
port = 1883
tag_temp = "TE4017/equipo8/Temperatura"
tag_hum = "TE4017/equipo8/Humedad"
tag_cO2 = "TE4017/equipo8/CO2"
tag_equipo = "TE4017/equipo8"

# Initial connection is Fase
Connected = False

# Init client
client = mqttClient.Client(mqttClient.CallbackAPIVersion.VERSION1)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, port)
client.loop_start()

while Connected != True:
    time.sleep(0.5)
    client.subscribe(tag_temp)
    client.subscribe(tag_hum)
    client.subscribe(tag_cO2)
    client.subscribe(tag_equipo)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Envio de datos detenido por el usuario")
        client.disconnect()
        client.loop_stop()