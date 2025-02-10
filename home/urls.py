from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.django_home, name='django_home'),
    # path('about/', views.django_about, name='django_about'),
    # path('services/', views.services, name='services'),
   
]
