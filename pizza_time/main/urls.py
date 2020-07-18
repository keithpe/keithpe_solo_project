from django.urls import path, include
from . import views

urlpatterns = [
    path('quick/', views.index),
    path('order/', views.order),
]
