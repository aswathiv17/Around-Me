from django.forms import Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']
        

class LogForm(forms.Form):
     username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":"Username","class":"form-control"}))
     password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control"}))