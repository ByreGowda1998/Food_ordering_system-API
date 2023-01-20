from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.homepage,name = 'home'),
    path('about/',views.aboutus ,name = 'about'),
    path('contact/' ,views.contact_us ,name ='contact'),
    path('loginto/',views.loginto,name='loginto'),
    path('register/',views.user_register ,name='register'),
    path('logout/',views.log_out,name='logout'),
    path('profile/',views.Profile,name="profile")
]