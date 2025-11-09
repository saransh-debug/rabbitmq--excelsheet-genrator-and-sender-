from django.shortcuts import render
from django.http import HttpResponse
from mailapp.mail import mailsender
# Create your views here.

def email_view(request):
    message = "hello this is a test message "
    subject = " TEST EMAIL "
    recipient_name= 'bhardwajsaransh8@gmail.com'
    mailsender(subject ,message, recipient_name)
    
    return HttpResponse("mail is sent ")