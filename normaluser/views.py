from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'normaluser/home.html')

def login(request):
    return render(request,'normaluser/Login.html')

def signup(request):
    return render(request,'normaluser/signup.html')