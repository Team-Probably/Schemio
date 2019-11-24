from django.urls import path, include
from . import views
urlpatterns = [ 
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.loginuser, name='login'), 
    path('logout/', views.logoutuser, name='logoutuser'),
    path('signup/verify', views.verify_email, name='verify_email'),
    path('', views.index, name='index'),
    path('editprofile', views.editprofile, name='editprofile')
    
    ]
