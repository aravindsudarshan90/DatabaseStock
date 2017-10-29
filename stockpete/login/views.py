from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponseRedirect
from django import forms
from forms import Loginform
from models import Login
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	  return render(request, 'login/login.html',)
def index1(request):
	  return render(request, 'login/done.html',)
def index3(request):
	  return render(request, 'login/test.html',)
#def index2(request):
#	 if request.method == 'POST':
#	 	  return HttpResponseRedirect(reverse('Buttons'))
#	 return render(request, 'login/done.html',)
def login(request):
     form=Loginform()    
     if request.method == 'POST':
        form =Loginform(request.POST)
        if form.is_valid():
          Usr=request.POST.get('Username')
          pwd=request.POST.get('Password')
          p=Login(Username=Usr, Password=pwd)
          p.save();
          return HttpResponseRedirect(reverse('Done'))
        else:
        	form=Loginform()
     return render(request, 'login/login.html', {'form' :form})
def Authen(request):
     form=Loginform()    
     if request.method == 'POST':
        form =Loginform(request.POST)
        if form.is_valid():
          Usr=request.POST.get('Username')
          pwd=request.POST.get('Password')
          log=Login.objects.all();
          for i in log:
          	if(i.Username==Usr and i.Password==pwd):
          		return render(request,'login/done.html',{'Logi':i})#HttpResponseRedirect(reverse('Done'))# render('login/done.html',{'Logi': i})HttpResponseRedirect(reverse('Done'),{'Logi' :i}) #redirect('/customer/done', {foo :'log'})#HttpResponseRedirect(reverse('Done'),{'Logi' :log})
          	else:
        	 form=Loginform()
     return render(request, 'login/login.html', {'form' :form})   
          	
			
        #   obj.save()
           
            #finally save the object in db
           

            #Username=Username,Password=Password

 #   else:
  #      form = Loginform()
   #     return render(request, 'login/login.html', {'form' :new_poll,})

  #  return render(request, 'login/login.html', {'form' :form,})
