from django.shortcuts import render

from django import forms
from models import Customer


class Inputform(forms.Form):
    class Meta:
        model = Customer
        #fields = ('Username','Password')

# Create your views here.
