from django import forms
from .models import *
  
  
class BioForm(forms.ModelForm):
    class Meta:
        model=Bio
        exclude=["user"]
        widgets={
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "gender":forms.Select(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "status":forms.TextInput(attrs={"class":"form-control"}),           
        }  
        
        
class ChangePasswordForm(forms.Form):
    current_password=forms.CharField(max_length=50,label="current password",widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control"}))
    new_password=forms.CharField(max_length=50,label="new password",widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control"}))
    confirm_password=forms.CharField(max_length=50,label="confirm password",widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control"}))
    
class PostForm(forms.ModelForm):
    class Meta:
        model=posts
        fields=["image","caption"]
        widgets={
            # "image":forms.FileInput(),
            "caption":forms.TextInput(attrs={"class":"form-control"}),
            
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=comments
        fields=["comment"]
        widgets={
        "comment":forms.Textarea(attrs={"class":"form-control"}),
            
        }
                        
                