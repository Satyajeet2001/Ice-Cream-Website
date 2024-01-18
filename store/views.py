from django.shortcuts import render
from datetime import datetime
from store.models import Contact
from django.contrib import messages
# Create your views here.


def home(request):
    messages.success(request,"Welcome to meridian icecreams.")
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # ,date=datetime.today())
        contact = Contact(name=name, email=email,
                          subject=subject, message=message)
        contact.save()
        messages.success(request, "Thanks for your valuable enquiry/feedback")
        
    return render(request, 'contact.html')


def buy(request):
    return render(request, 'buy.html')
