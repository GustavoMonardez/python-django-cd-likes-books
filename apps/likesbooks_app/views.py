from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "likesbooks_app/index.html")