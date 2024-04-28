from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request,'root/index.html')

def offers(request):
    return render(request,'root/offers.html')

def contact(request):
    return render(request,'root/contact_us.html')


def about(request):
    return render(request,'root/about.html')

