from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        user = request.POST['Username']
        password = request.POST['password']
        adminuser = auth.authenticate(username = user,password = password)

        if adminuser is not None:
            auth.login(request,adminuser)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        a = request.POST['Username']
        b = request.POST['first_name']
        c = request.POST['last_name']
        d = request.POST['email-id']
        e = request.POST['password']
        f = request.POST['confirm_password']
        if e == f:
            if User.objects.filter(username = a).exists():
                messages.info(request,'Username taken')
                return redirect('registration')
            elif User.objects.filter(email = d).exists():
                messages.info(request,'Email address taken')
                return redirect('registration')
            else:
                demo_user = User.objects.create_user(username=a,password=e,first_name=b,last_name=c,email=d)
                demo_user.save();
                print('User created')
                return redirect('login')
        else:
            messages.info(request,'Password not matched')
            return redirect("registration")
        return redirect('/')
    return render(request,'registration.html')
def logout(request):
    auth.logout(request)
    return redirect('/')