# app urls

from django.urls import path
from . import views

app_name = 'comictextmaker' 
urlpatterns = [
    
    path('', views.index, name = 'index'),
    path('home/',views.home, name = 'home'),
    path('yourcomic/', views.story, name = 'yourcomic'),
    path('about/', views.about, name = 'about'),

]
