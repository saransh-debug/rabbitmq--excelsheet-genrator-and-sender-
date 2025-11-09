import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rabitmqtest.settings")  # ✅ Use your actual project name
django.setup()

import pika
import json
import pandas as pd 
import uuid
import os 
from django.core.mail import EmailMessage 
from django.conf import settings

def genrate_excel(message):
    data = message['data']
   
    data = pd.DataFrame(data)   
    print(data)
    
    
    if os.path.exists('excelfiles'):
        data.to_excel(f"excelfiles/excel{uuid.uuid4()}.xlsx", index=False )
    else:
        os.makedirs('excelfiles')
        data.to_excel(f"excelfiles/excel{uuid.uuid4()}.xlsx", index=False )
        
def mailfunc(message ):
        
        
        print("reached message")
        mail= EmailMessage(
            subject = message['subject'] , 
            body = message['message'] , 
            from_email=settings.EMAIL_HOST_USER ,
            to=[message['recipient_email']],
            
        )
        folder_path = r'C:\projects\rbmq\excelfiles'
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path , filename)
            if os.path.exists(file_path) and os.path.isfile(file_path):
                mail.attach_file(file_path)
                mail.send()
            else:
                print("path doesnt exists")

def callback(ch ,properties , method , body ):
    print('consumer started:')
    message  = body.decode()
    message = json.loads(message)
    print(message)
    print(type(message))
    if message['type'] == "email":
        print(message)
        print('sent to the mail')
        mailfunc(message)
    elif message['type'] =='excel':
        print("reached the excel calling function ")
        genrate_excel(message)
    else:
        print(message.get('type'))
    
    
    
 
        
    
    
    
params = pika.URLParameters("amqps://bzozctwh:XIs8_0ftEeG4HRmNc5EspDMxH5iEO2Ja@campbell.lmq.cloudamqp.com/bzozctwh")
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='my_queue')
channel.queue_declare(queue='mail_queue')
channel.basic_consume(
    queue='my_queue',
    on_message_callback=callback,
    auto_ack=True
)

channel.basic_consume(
    queue='mail_queue',
    on_message_callback=callback,
    auto_ack=True
)


channel.start_consuming()