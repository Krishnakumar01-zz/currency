from django.shortcuts import render,redirect,get_object_or_404
from .models import Currency
from .forms import CurrencyForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
import requests
from django.http import JsonResponse
import unicodedata
from django.utils import timezone




# Create your views here.
def home(request):
	return render(request,'converter/home.html')

def conversion(request):
	if request.method=='POST':
		form=CurrencyForm(request.POST)
		fromm=request.POST['fromm']
		to=request.POST['to']
		link="https://api.fixer.io/latest?base="
		s=link+fromm
		result=requests.get(s)
		rates=result.json()
		output=rates['rates'][str(to)]
		date=timezone.now()
		ans=str(fromm)+" to "+str(to)+' at '+str(date)
		Currency.objects.create(data=ans)
		return render(request,'converter/output.html',{'output':output})
	else:
		link="https://api.fixer.io/latest"
		result=requests.get(link)
		res=result.json()
		symbols=res['rates'].keys()
		out=[]
		for i in symbols:
			out.append(unicodedata.normalize('NFKD', i).encode('ascii','ignore'))
		form=CurrencyForm()
		return render(request,'converter/conversion.html',{'form':form,'symbols':out})
		
def signup(request):
	if request.method=='POST':
		form =UserCreationForm(request.POST)
		if form.is_valid():
			obj=form.save(commit=False)
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password1')
			obj=form.save()
			user=authenticate(username=username,password=password)
			login(request,user)
			return redirect('conversion')
		else:
			print("not possible")	
	else:
		form=UserCreationForm()
		return render(request,'converter/signup.html',{'form':form})	

def signin(request):
	if request.method=='POST':
		form=AuthenticationForm(request.POST)
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('conversion')
	else:
		form=AuthenticationForm()
		return render(request,'converter/signin.html',{'form':form})
def signout(request):
	logout(request)
	return render(request,'converter/home.html')		