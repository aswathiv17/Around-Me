from django.urls import path
from .views import *

urlpatterns =[
    path('home/',UserHome.as_view(),name="uh"),
    path('profile/',profileView.as_view(),name="pro"),
    path('bio/',BioView.as_view(),name="bio"),
    path('editbio/<int:pk>/',EditBioView.as_view(),name="ebio"),
    path('cp/',ChangePassword.as_view(),name="cp"),
    path('post/',PostView.as_view(),name="post"),
    path('editpost/<int:pk>/',EditPostView.as_view(),name="pedit"),
    path('delp/<int:pk>/',DeletePostView.as_view(),name="dp"),
    path('addcmnt/<int:pid>/',addcomment,name="addc"),
    path('addlike/<int:pid>/',addlike,name="like")


    



]