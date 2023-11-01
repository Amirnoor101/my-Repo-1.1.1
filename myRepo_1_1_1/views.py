from django.http import HttpResponse

def amirtest (request) :
    return HttpResponse ('<h1> This is a test </h1>')