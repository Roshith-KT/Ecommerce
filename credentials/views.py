from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.http import HttpResponseRedirect,HttpResponse
from .emails import send_account_activation_email,send_password_reset_otp
from.models import Profile
import uuid
import random
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password


# Create your views here.

@login_required(login_url='credentials:login')
def logout(request):
    auth.logout(request)
    return redirect('credentials:login')

def login(request):
    if request.user.is_authenticated:
        return redirect('wholeshopview:home')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            try:
                profile=Profile.objects.get(user=user)
            except Profile.DoesNotExist:
                messages.info(request,"No such user")
                return redirect('credentials:login')
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
                my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
                my_customer_group[0].user_set.add(user)
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


def password_reset(request):
    if request.method=='POST':
        email=request.POST['email']
        password_reset_otp(email)
        return redirect('credentials:password_reset_page', email=email)

    return render(request,'credentials/password_reset.html')


def password_reset_otp(email):
    user=User.objects.get(email=email)
    profile=Profile.objects.get(user=user)
    profile.otp=random.randint(1000, 9999)
    profile.save()
    send_password_reset_otp(email,profile.otp)


def password_reset_page(request,email):
    if request.method == 'POST':
        otp=request.POST['otp']
        new_password=request.POST['new_password']
        user=User.objects.get(email=email)
        profile=Profile.objects.get(user=user)
        if int(otp)==profile.otp:
            user.set_password(new_password)
            user.save()
            messages.info(request,"Password is successfully updated")
            return HttpResponseRedirect(request.path_info)
        else:
            messages.info(request,'Invalid OTP')
            return HttpResponseRedirect(request.path_info)
    return render(request,'credentials/password_reset_page.html')



def profile(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        mobile=request.POST['mobile']
        address=request.POST['address']
        post_code=request.POST['post_code']
        area=request.POST['area']
        email=request.POST['email']
        country=request.POST['country']
        state=request.POST['state']
        user=request.user
        profile=Profile.objects.get(user=user)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        profile.mobile=mobile
        profile.address=address
        profile.save()
        return redirect('/')
        
    
    context={
        "user":user,
        "profile":profile
    }
    return render(request,'credentials/profile.html',context)


def change_password(request):
    if request.method=="POST":
        user=request.user
        current_password=request.POST['current_password']
        new_password=request.POST['new_password']
        
        if check_password(current_password, user.password):
            user.set_password(new_password)
            user.save()
            messages.info(request, 'Password Updated Successfully')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.info(request,'Error! Check credentials provided and retry later')
            return HttpResponseRedirect(request.path_info)
    return render(request,'credentials/change_password.html')



def admin_login(request):
    if request.user.is_authenticated:
        return redirect('ecomadmin:ecomadmin_dash')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            try:
                profile=Profile.objects.get(user=user)
                if profile:
                    messages.info(request,"Invalid Credentials.. Check Your credentials")
                    return redirect('credentials:admin_login')
            except Profile.DoesNotExist:
                auth.login(request, user)
                return redirect('ecomadmin:ecomadmin_dash')
        else:
            messages.warning(request, "Invalid credentials")
            return HttpResponseRedirect(request.path_info)
    return render(request,'ecomadmin/admin_login.html')


#function for providing restrictions amoung customers and admin 

# def is_admin(user):
#     if user.is_staff:
#         return True

# def is_customer(user):
#     return user.groups.filter(name='CUSTOMER').exists()
    

# def after_login(request):
#     if is_customer(request.user):
#         return redirect('wholeshopview:home')
#     else:
#         return redirect('ecomadmin:ecomadmin_dash')