from django.urls import path, include
from . import views

urlpatterns = [
    path('quick/', views.index),
    path('order/', views.order),
    path('order/favorite/', views.order_favorite),
    path('order/surprise/', views.order_surprise),
    path('order/add_item/', views.order_add_item),
    path('order/process/', views.order_process),
    path('order/checkout/', views.order_checkout),
]
