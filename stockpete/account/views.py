from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponseRedirect
from django import forms
from forms import LoginInputform
from models import Account
import datetime
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	  return render(request, 'accounts/login.html',)
def index1(request):
	  return render(request, 'accounts/autheninput.html',)
def index3(request):
	  return render(request, 'accounts/authen.html',)
def login(request):
     form=LoginInputform()    
     if request.method == 'POST':
        form =LoginInputform(request.POST)
        if form.is_valid():
          Usr=request.POST.get('Username')
          pwd=request.POST.get('Password')
          p=Account(Username=Usr,password_hash=pwd,create_date=datetime.date.today())
          p.save();
          return render(request,'accounts/done.html')
         # return HttpResponseRedirect(reverse('Created'))
        else:
        	form=LoginInputform()
     return render(request, 'accounts/autheninput.html', {'form' :form})
def Authen(request):
     form=LoginInputform()    
     if request.method == 'POST':
        form =LoginInputform(request.POST)
        if form.is_valid():
          Usr=request.POST.get('Username')
          pwd=request.POST.get('Password')
          log=Login.objects.all();
          for i in log:
          	if(i.Username==Usr and i.password_hash==pwd):
          		return render(request,'accounts/done.html',{'Logi':i})#HttpResponseRedirect(reverse('Done'))# render('login/done.html',{'Logi': i})HttpResponseRedirect(reverse('Done'),{'Logi' :i}) #redirect('/customer/done', {foo :'log'})#HttpResponseRedirect(reverse('Done'),{'Logi' :log})
          	else:
        	 form=LoginInputform()
     return render(request, 'login/authen.html', {'form' :form})   
