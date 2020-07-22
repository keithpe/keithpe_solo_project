from django.urls import path, include
from . import views

urlpatterns = [
    path('quick/', views.index),
    # path('order/', views.order),
    path('order/favorite/', views.order_favorite),
    path('order/surprise/', views.order_surprise),
    path('order/new/', views.order_new),
    path('order/create/', views.order_create),
    path('order/item/new/', views.item_new),
    path('order/item/create/', views.item_create),
    path('order/process/', views.order_process),
    path('order/checkout/', views.order_checkout),
]
