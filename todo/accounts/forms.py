from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class CustomUserRegister(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password'}))
    class Meta:
        model=User  
        fields = ['username','email','password1','password2',]