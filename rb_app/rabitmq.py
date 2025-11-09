import pika
import json


def dummy(message ):
    message = json.dumps(message )
    params = pika.URLParameters("amqps://bzozctwh:XIs8_0ftEeG4HRmNc5EspDMxH5iEO2Ja@campbell.lmq.cloudamqp.com/bzozctwh")
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='my_queue')
    
    channel.basic_publish(
        
        exchange='',
        routing_key="my_queue",
        body=message
    )
    
    # print(f"the message published is :{message}")
    connection.close()