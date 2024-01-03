from django.shortcuts import render,redirect
from .models import Donation
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def HomePage(request):
    return render(request,'index.html')
def donation(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        message=request.POST['message']
        donate=Donation.objects.create(First_name=fname,Last_name=lname,Email=email,Message=message)
        donate.save()
        subject = 'Donation Submmission'
        body = f'Hi Am: {fname} {lname}\n\nMy Email: {email} \n\n Message: {message}'
        from_email=email
        recipient_list = [settings.EMAIL_HOST_USER ]
        send_mail(subject, body, email, recipient_list)

        messages.success(request,'Personal Infromation sent Successfull')
    else:
        messages.error(request,"Something went Wrong")
        

    return render(request,'donate.html')