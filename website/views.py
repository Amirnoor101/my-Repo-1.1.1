from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse as res

def index_views (request) :
    return res ('<h1>Home page<h1\>')
def about_views (request) :
    return res ('<h1>I124Q<h1\>')
def contact_views (request) :
    return res ('<h1>Crazy<h1\>')