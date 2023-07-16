from django.shortcuts import render,redirect
from . import models
from .models import *
from django.contrib import messages
from django.http.response import HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,"home.html")
@login_required(login_url="/login/")
def about(request):
    return render(request,"about.html")
@login_required(login_url="/login/")
def knee(request):
    return render(request,"knee.html")
@login_required(login_url="/login/")
def padmasana(request):
    return render(request,"padmasana.html")


@login_required(login_url="/login/")
def video(request):
	return render(request,'videos.html')
@login_required(login_url="/login/")
def contact(request):
	return render(request,'contact.html')
def login(request):
	if request.method=='POST':
		uname = request.POST.get('uname',"Guest (or whatever)")
		pwd = request.POST.get('pwd',"Guest (or whatever)")
		user=auth.authenticate(username=uname,password=pwd)

		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			messages.info(request,"invalid credentials")
			return redirect('login')
	else:
		return render(request,'login.html')
def register(request):
	if request.method =='POST':
		username = request.POST.get('username',"Guest (or whatever)")
		password = request.POST.get('password',"Guest (or whatever)")
		cpassword = request.POST.get('cpassword',"Guest (or whatever)")

		if(password==cpassword):
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username is already existed')
				return redirect('login')
			else:
				user=User.objects.create_user(username=username,password=password)
				user.save();
				print('User created')
				return redirect('login')
		else:
			messages.info(request,'password is not matching')
			print('pword not matching')
			return redirect('login')
		return redirect('home')

	else:
		return render(request,'login.html')


def logout(request):
	auth.logout(request)
	return redirect('home')
@login_required(login_url="/login/")
def yogaguru(request):
    if request.method=='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        find=request.POST.get('find')
        User_det.objects.create(name=name,age=age,email=email,find=find)
        det=Asanas.objects.filter(Symptoms=find).values()
        context={
            'name':name,
            'age':age,
            'email':email,
            'find':find,
            'det':det,
        }
        return render(request,"solution.html",context)
            
    else:
        return render(request,"yogaguru.html")
def solution(request):
    return render(request,"solution.html")
