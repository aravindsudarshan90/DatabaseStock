from django.shortcuts import render

from django import forms
from models import Login


class Loginform(forms.Form):
    class Meta:
        model = Login
        #fields = ('Username','Password')

# Create your views here.
