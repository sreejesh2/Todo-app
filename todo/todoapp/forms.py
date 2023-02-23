from django.forms import ModelForm
from django import forms
from .models import Todo

class Todoform(ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control',"placeholder":"Title"}))
    discription = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control',"placeholder":"Discription"}))
    class Meta:
        model=Todo
        fields=['title','discription']