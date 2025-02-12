
from django.urls import path
from home import views
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about_page, name='about_page'),
    
     
]