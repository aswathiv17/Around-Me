from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

# class MainHome(View):
#     def get(self,request,*args, **kwargs):
#         return render(request,"mainhome.html")
         
class MainHome(TemplateView):
    template_name="mainhome.html" 
            
         
         
# class RegView(View):
#     def get(self,request,*args, **kwargs): 
#         f=RegForm()
#         return render(request,"reg.html",{"form":f})
#     def post(self,request,*args,**kwargs):
#             form_data=RegForm(data=request.POST)
#             if form_data.is_valid():
#                 form_data.save()
#                 messages.success(request,"registration successfull")
#                 return redirect("h")
#             else:
#                  messages.error(request,"registration failed")
#                  return render(request,"reg.html",{"form":form_data})

    
class RegView(CreateView):
    form_class=RegForm
    template_name="reg.html"
    model=User
    success_url=reverse_lazy("h")   
    
    
    
class LogView(FormView):
     template_name="log.html"
     form_class=LogForm
     def post(self,request,*args,**kwargs):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("username")
            ps=form_data.cleaned_data.get("password")
            user=authenticate(request,username=un,password=ps)
            if user:
                  login(request,user)
                  messages.success(request,"Login Successfull")
                  return redirect("uh")
            else:
                   messages.error(request,"Login Failed!! Username or Password incorrect ")
                   return render(request,"log.html",{"form":form_data})
        else:
               messages.error(request,"Login Failed!! ")
               return render(request,"log.html",{"form":form_data})           
           
class LogOut(View) :
    def get(self,request):
        LogOut=(request)
        return redirect("log.html")