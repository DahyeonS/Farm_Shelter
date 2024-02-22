from django.shortcuts import render

from func.cheese import *

# Create your views here.
def index(request) :
    return render(request, 'index.html')