from django.core.mail import send_mail ,EmailMessage
from django.conf import settings
import os 
import pika 
import json 






def mailsender(recived_subject , recieved_message , recipient_email):
    
    params = pika.URLParameters("amqps://bzozctwh:XIs8_0ftEeG4HRmNc5EspDMxH5iEO2Ja@campbell.lmq.cloudamqp.com/bzozctwh")
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='mail_queue')
    
    data = {
        "type":"email",
        "subject":recived_subject , 
        "message":recieved_message,
        "recipient_email":recipient_email
    }
    
    j_data = json.dumps(data)
    channel.basic_publish(
        exchange='',
        routing_key="mail_queue",
        body=j_data
    )
    # print(f"the message published is :{message}")
    connection.close()
    
    
    
    
    
    
    
    
    