from django.shortcuts import render, redirect, HttpResponse

def index(request):
        return HttpResponse("This is the Pizza Time Main Page")
