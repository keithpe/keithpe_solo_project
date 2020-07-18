from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return render(request, 'index.html')


def order(request):
    return render(request, 'order.html')
