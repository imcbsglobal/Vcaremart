from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
    path('branch/', views.branch, name='branch'),
    path('contact/', views.contact, name='contact'),
     path('privacy/', views.privacy, name='privacy'),
    

]

