from django.shortcuts import render

from func.farm_map import *

# Create your views here.
def farm_list(request) :
    return render(request, 'farm/farm_list.html')

def map(request) :
    return render(request, 'farm/map.html')

def detail(request, id) :
    content = get_farm(id)
    return render(request, 'farm/farm.html', content)