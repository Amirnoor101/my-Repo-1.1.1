from django.http import HttpResponse as res

def testy (request) :
    return res ('Hello world')