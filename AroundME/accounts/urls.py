from django.urls import path
from accounts.views import*

urlpatterns = [
    path('reg/',RegView.as_view(),name="reg"),
    path('log/',LogView.as_view(),name="log"),
    path('logout/',LogOut.as_view(),name="logout"),
]

