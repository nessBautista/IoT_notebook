import pika
# Este script se encarga de publicar un mensaje a una cola de trabajo de RabbitMQ.

# Establecemos la conexión a RabbitMQ que esta corriendo en nuestro localhost
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

# Necesitamos crear una conexión a un canal para poder enviar mensajes
channel = connection.channel()

# Ahora creamos una cola de trabajo
channel.queue_declare(queue='IoT_Equipo8')


# Publicamos nuestro mensaje
channel.basic_publish(
    exchange='',
    routing_key='IoT_Equipo8',
    body= 'Hola desde python script! - 14 de marzo 2024'
)
print(" our message was published")

# Finalmente cerramos la conexión
connection.close()