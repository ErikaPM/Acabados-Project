from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('services/', views.services, name='blog-services'),
    path('quotes/', views.quotes, name='blog-quotes'),
    path('contact/', views.contact, name='blog-contact'),
    path('login/', views.login, name='blog-login'),
    path('calculator/', views.calculator, name='blog-calculator'),
]
