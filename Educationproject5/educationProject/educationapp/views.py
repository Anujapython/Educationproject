from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import registers,logins,formss

# Create your views here.

def demo(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        l=logins(username=username,password=password)
        l.save()
        return redirect('new')
    else:
        return render(request,'login.html')

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        p=registers(username=username,password=password)
        messages.info(request,'please specified your record')
        p.save()
        return redirect('login')
    else:
        return render(request,'register.html')
# Create your views here.


def form(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phoneno= request.POST.get('phoneno')
        f=formss(name=name,dob=dob,age=age,gender=gender,email=email,address=address,phoneno=phoneno)
        f.save()
        return redirect('new2')
    return render(request, 'form.html')

def new(request):
    return render(request,'new.html')

def new2(request):
    return render(request,'new2.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

