from django.shortcuts import render
from . models import *
from django.http import JsonResponse

# Create your views here.def home(request):
def home(request):
    

    return render(request, 'index.html' , {})

