from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #new

def homePageView(request): #new
    return HttpResponse("Hello World!")  # new    