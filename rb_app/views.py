from django.shortcuts import render
from rb_app.rabitmq import dummy
import random
from faker import Faker 

fake = Faker()

def home(request):
    message = f"this is message no {random.randint(1,100)}"
    
    details  = []
    
    for _ in range(1,10):
        details.append({
            
            "name":fake.name(),
            "address":fake.address()
        })
        
    x = {"type":"excel",
         "data":details}
    print(x)
    dummy(x)
    return render(request , 'index.html' , {'message':message})