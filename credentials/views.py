from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from .emails import send_account_activation_email
from.models import Profile
import uuid
# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('credentials:login')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            profile=Profile.objects.get(user=user)
            if profile.is_email_verified is True:
                auth.login(request, user)
                return redirect('wholeshopview:home')
            else:
                messages.warning(request,"Please verify your account inorder to login")
                return HttpResponseRedirect(request.path_info)
        else:
            messages.warning(request, "Invalid credentials")
            return HttpResponseRedirect(request.path_info)
    return render(request,'credentials/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists():
                messages.warning(request, "Username and Email are already taken")
                return HttpResponseRedirect(request.path_info)
            elif User.objects.filter(username=username).exists():
                messages.warning(request, "Username taken")
                return HttpResponseRedirect(request.path_info)
            elif User.objects.filter(email=email).exists():
                messages.warning(request, "email taken")
                return HttpResponseRedirect(request.path_info)
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                profile=Profile.objects.create(user=user,email_token=str(uuid.uuid4()))
                profile.save()
                send_account_activation_email(email,profile.email_token)
                
                messages.info(request,"Account created successfully, Check your Mail and Verify Your Email inorder to Login!!!")
                return HttpResponseRedirect(request.path_info)
            
        else:
            messages.warning(request, "Password not matching")
            return HttpResponseRedirect(request.path_info)
        
    return render(request,'credentials/register.html')


def activate_account(request,email_token):
    profile=Profile.objects.get(email_token=email_token)
    profile.is_email_verified=True
    profile.save()
    return redirect('credentials:login')
    