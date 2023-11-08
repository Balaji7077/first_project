from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jampandu(request):
    return HttpResponse('<h1><marquee>hiii:hi jampandu how are u</h1></marquee>')

def junglerani(request):
    return HttpResponse('<h1><marquee>replay:iam fine</h1><marquee>')