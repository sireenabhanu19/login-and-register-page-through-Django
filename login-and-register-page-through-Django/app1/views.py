from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from app1.models import tweet

# Create your views here.
def home(request):
    return render(request,'index.html')


def loginV(request):
    if request.user.is_authenticated:
        messages.warning(request,"Mama you already logged! ")
        return redirect('homepage')
    #logout(request)
    if request.method=="POST":
        a=request.POST.get('ip1')
        b=request.POST.get('ip2')
        result=authenticate(request,username=a,password=b)
        if result is not None:
            print(a,b,type(result))
            login(request,result)
            messages.success(request,"Thank you for coming back ! ")
            return redirect('profilepage')
        else:
            messages.error(request,"are you trying to cheat me ! Wrong creds")
            return redirect('loginpage')
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')
@login_required(login_url='loginpage')
def postv(request):
    return render(request,'post.html')
@login_required(login_url='loginpage')
def tweets(request):
    if request.method=="POST":
        m=request.POST.get('msg')
        obj=tweet(uname=str(request.User.username),post=m)
        obj.save()  
        result=tweet.objects.all()
        return render(request,'tweet.html')
    return render(request,'tweet.html')

def register(request):
    if request.user.is_authenticated:
        messages.warning(request,"Man you already have an account !")
        return redirect('homepage')
        
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        passw=request.POST.get('passw')
        cpass=request.POST.get('cpass')
        email=request.POST.get('email')
        uname=request.POST.get('uname')
        print(fname,lname,passw,cpass,email,uname)

        #validation username
        if User.objects.filter(username=uname).exists():
            messages.error(request,"Username already exists !")
            return redirect('loginpage')
        #validation for password
        if len(passw)<8:
            messages.error(request,"Password must be 8 chars")
            return redirect('registerpage')
        #validation for cpass
        if (cpass!=passw):
            messages.error(request,"Passwords doest match")
            return redirect('registerpage')

        obj=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=passw)
        obj.save()
        messages.success(request,"Hey your account is ready, Login now")
        return redirect('loginpage')

    return render(request,'register.html')

def logoutV(request):
    logout(request)
    messages.info(request,"are you leaving me ! you cheat")
    return redirect('loginpage')
