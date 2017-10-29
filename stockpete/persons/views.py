
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django import forms
from forms import Inputform
from models import Customer
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	  return render(request, 'persons/login1.html',)
def index1(request):
	  return render(request, 'persons/index.html',)
def index2(request):
	  return render(request, 'persons/registration.html',)
def index3(request):
	  return render(request, 'persons/account.html',)
def login(request):
     form=Inputform()    
     if request.method == 'POST':
        form =Inputform(request.POST)
        if form.is_valid():
          Usr=request.POST['fname']
          pwd=request.POST['lname']
          pnum=request.POST['pnum']
          addr=request.POST['addr']
          city=request.POST['city']
          state=request.POST['state']
          zcode=request.POST['zcode']
          email=request.POST['email']
          rating=request.POST['rating']
          
          p=Customer(first_name=Usr, last_name=pwd, ph_num=pnum, address=addr, city=city, state=state, zip_code=zcode, email=email, rating=rating)
          p.save();
          return render(request, 'accounts/autheninput.html')
          #return redirect((reverse('ha')))#HttpResponseRedirect
        else:
        	form=Inputform()
     return render(request, 'persons/login.html', {'form' :form})
