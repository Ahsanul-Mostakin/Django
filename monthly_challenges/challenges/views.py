from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def january(request):
    return HttpResponse("Eat no meat for entire month!")


def february(request):
    return HttpResponse("Walk for 20 miniutes everyday!")
