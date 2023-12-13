from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def std(request):
    return HttpResponse("hello.....")