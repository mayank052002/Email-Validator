from django.shortcuts import render
import requests
import os
from django.http import HttpResponse
def process_email(request,email):
	start="http://apilayer.net/api/check?access_key=421ecfa067fcbe50e9bb7f822fa21b75&email="+email
	data=requests.get(start)
	data=data.json()
	return render(request,'info.html',{'data':data})
def get_email(request):
	data={
		'msg':""
		}
	email=request.POST.get("Email")
	if email is None:
		data={
		'msg':"Please Enter The Email Address"
		}
	elif len(email) == 0:
		data={
		'msg':"Please Enter The Email Address"
		}
	else:
		return process_email(request,email)

	

	return render(request,'home.html',{'data':data})
	
		
	

