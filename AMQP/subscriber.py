import pika

# Establecemos la conexión a RabbitMQ que esta corriendo en nuestro localhost
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

# Necesitamos crear una conexión a un canal para poder enviar mensajes
channel = connection.channel()

# Ahora creamos una cola de trabajo
channel.queue_declare(queue='IoT_Equipo8')

# Definimos una función para administrar el callback de nuestro canal
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Nos suscribimos a nuestra queue
channel.basic_consume(
    queue='IoT_Equipo8',
    on_message_callback=callback,
    auto_ack=True
)

print(" [*] Waiting for messages. To exit press CTRL+C")
# Comenzamos la subscripción
channel.start_consuming()