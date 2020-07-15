from django.urls import path, include
from . import views

urlpatterns = [
    path('pizza', views.pizza),
]
