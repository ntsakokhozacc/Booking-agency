from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

#login view with validations
def login(request):
    if request.method== "POST":
        username=request.POST['username']
        password=request.POST['password']

        #authenticating if whether the issue is authorised
        user = auth.authenticate(username=username, password=password)

        #if user is authorised
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        #if user is not authorized the message will be returned
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')


#rigistration view with validations
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                   messages.info(request,'Email Taken')
                   return redirect('register')
            else:
                user=User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')  
        return redirect('/')
    else:
        return render(request, 'register.html')


    def logout(request):
        auth.logout(request)
        return redirect("/")