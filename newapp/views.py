from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'newapp/index.html')

def about(request):
    return render(request, 'newapp/about.html')

def contact(request):
    return render(request, 'newapp/contact.html')

def register(request):
    return render(request, 'newapp/register.html')

def user_login(request):
    return render(request, 'newapp/login.html')