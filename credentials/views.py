from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'credentials/login.html')

def register(request):
    return render(request,'credentials/register.html')

def logout(request):
    pass

