from django.shortcuts import render, redirect, HttpResponse


def index(request):
    print('Quick Options')
    return render(request, 'index.html')


def order(request):
    print('Order selected')
    return render(request, 'order.html')


def order_favorite(request):
    print('Order FAVORITE selected')
    return render(request, 'order.html')


def order_surprise(request):
    print('Order SURPRISE selected')
    return render(request, 'order.html')


def order_process(request):
    print('Process order')
    # Process the order and
    return render(request, 'checkout.html')


def order_checkout(request):
    print('Checkout')
    return render(request, 'checkout.html')
