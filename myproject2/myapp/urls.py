from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('home', views.home, name='blog-home'),
    path('blogs/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
]