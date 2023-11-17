from django.shortcuts import render
from django.http import HttpResponse as res



# Funcs

def index_views (request) :
    return render (request,'index.html')

def about_views (request) :
    return render (request,'about.html')

def contact_views (request) :
    return render (request,'contact.html')