from django.shortcuts import render,redirect
from .models import Donation
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import datetime
from datetime import datetime
# Create your views here.
def HomePage(request):
    year = datetime.now().year
    return render(request,'index.html',{'Years':year})
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
        print("Something went Wrong")
        
    year = datetime.now().year
    return render(request,'donate.html',{'Years':year})
def volunteer(request):
    year = datetime.now().year
    return render(request,'volunteer.html',{'Years':year})
def SpansorShip(request):
    year = datetime.now().year
    return render(request,'Sponsorship.html',{'Years':year})
def Mission(request):
    return render(request,'mission.html')
def ourStory(request):
    return render(request,'our-story.html')
def socail_support(request):
    return render(request,'socail_support.html')
def art(request):
    return render(request,'art.html')
def contact (request):
    return render(request,'contact.html')