from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('signup', views.signup, name="signup"),
   path('events', views.events, name="events"),
   path('contact', views.contact, name="contact"),
   path('about', views.about, name="about"),
   path('carrom_form', views.carrom_form, name="Carrom_form"),
   path('cricket_form', views.cricket_form, name="cricket_form"),
]