from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('category/',views.category,name='category'),
    path('about/',views.about,name='about'),
    path('contact',views.contact,name='contact'),
]