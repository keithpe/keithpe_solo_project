from django.shortcuts import render, redirect, HttpResponse


def pizza(request):
    return render(request, 'pizza.html')
