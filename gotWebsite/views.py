from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def home(request):
    return render(request,"gotWebsite/index.html")

def signup(request):
    return render(request,"gotWebsite/signup.html")

def events(request):
    return render(request,"gotWebsite/events.html")

def contact(request):
    return render(request,"gotWebsite/contact1.html")

def about(request):
    return render(request,"gotWebsite/about.html")

def carrom_form(request):
    return render(request,"gotWebsite/carrom_form.html")

def cricket_form(request):
    return render(request,"gotWebsite/cricket_form.html")