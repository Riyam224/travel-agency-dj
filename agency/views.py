from django.conf import settings
from django.shortcuts import render

# Create your views here.
from .models import Destination
from django.core.mail import send_mail
from django.conf import settings
from .filters import DestinationFilter



def index(request):

    dests = Destination.objects.all()
    myfilter = DestinationFilter(request.GET , queryset=dests)
    dests = myfilter.qs
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']


        send_mail(
            name,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
    return render(request  , 'index.html', {'dests': dests , 
    'myfilter': myfilter,})