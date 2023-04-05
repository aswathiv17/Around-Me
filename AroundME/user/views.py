from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,UpdateView,FormView,DeleteView
from .forms import *
from  django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,logout
# Create your views here.

class UserHome(CreateView):
    template_name='User_home.html'
    form_class=PostForm
    model=posts
    success_url=reverse_lazy("uh")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"post uploaded") 
        return super().form_valid(form) 
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=posts.objects.all().order_by('-datetime')
        context["cform"]=CommentForm()
        context["comments"]=comments.objects.all()
        return context
def addcomment(request,*args,**kwargs):
    if request.method=="POST":
            pid=kwargs.get("pid")
            post=posts.objects.get(id=pid)
            user=request.user
            cmnt=request.POST.get("comment")
            comments.objects.create(comment=cmnt,user=user,post=post)
            return redirect("uh")
        
def addlike(request,*args,**kwargs):
    pid=kwargs.get("pid")
    post=posts.objects.get(id=pid)
    user=request.user
    post.likes.add(user)
    post.save()
    return redirect("uh")


        
        
     

    
class profileView(TemplateView):
    template_name="profile.html"
    
class BioView(CreateView):
    form_class=BioForm
    template_name="bio.html"  
    model=Bio
    success_url=reverse_lazy("pro") 
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.object=form.save()
        messages.success(self.request,"bio added") 
        return super().form_valid(form) 
    
class EditBioView(UpdateView):
    form_class=BioForm
    model=Bio
    template_name="editbio.html"
    success_url=reverse_lazy("pro")
    pk_url_kwargs="pk"
           
class ChangePassword(FormView):
    template_name="ChangePassword.html"
    form_class=ChangePasswordForm
    def post(self,request,*args, **kwargs):
        form_data=ChangePasswordForm(data=request.POST)
        if form_data.is_valid():
            current=form_data.cleaned_data.get("current_password")
            new=form_data.cleaned_data.get("new_password")
            confirm=form_data.cleaned_data.get("confirm_password")
            print(current)
            user=authenticate(request,username=request.user.username,password=current)
            if user:
                if new==confirm:
                    user.set_password(new)
                    user.save()
                    messages.success(request,"password changed")
                    logout(request)
                    return redirect("log")
                else:
                    messages.error(request,"passwords mismatches")
                    return redirect("cp")
            else:
                    messages.error(request,"passwords INCORRECT")
                    return redirect("cp")
        else:
            return render(request,"changepassword.html",{"form":form_data})
        
class PostView(TemplateView):
    template_name="myposts.html"    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=posts.objects.filter(user=self.request.user).order_by('-datetime')
        return context
    
class EditPostView(UpdateView):
    form_class=PostForm
    model=posts
    template_name="editpost.html"
    success_url=reverse_lazy("post")
    pk_url_kwargs="pk"
           
         
class DeletePostView(DeleteView):
    model=posts
    template_name="deletepost.html"
    success_url=reverse_lazy("post")
    
    
    
    
        

    
    