from django.shortcuts import render

from django import forms
from models import Account


class LoginInputform(forms.Form):
    class Meta:
        model = Account
        #fields = ('Username','Password')

# Create your views here.
