from django.shortcuts import render, redirect
from django.contrib import messages
from urllib.parse import quote, unquote

from func.cheese import *
from farm.models import Cheese_detail
from farm.forms import CheeseForm

# Create your views here.
def cheese_list(request) :
    return render(request, 'cheese/cheese_list.html')

def detail(request, id) :
    name = Cheese_detail.objects.get(id=id).name
    story = Cheese_detail.objects.get(id=id).story
    recipe = Cheese_detail.objects.get(id=id).recipe
    url = Cheese_detail.objects.get(id=id).url

    return render(request, 'cheese/cheese.html', {'name': name, 'story': story, 'recipe': recipe, 'url': url})

def result(request) :
    if request.method == 'POST' :
        form = CheeseForm(request.POST, request.FILES)
        if form.is_valid() :
            file = form.cleaned_data['saveFile']
            new_name = image_upload(file)
            result = cheese_test(new_name)
            data = quote(result)

            url = 'proceed?value=' + data
            return render(request, 'cheese/proceed.html', {'url': url})
        else :
            messages.error(request, '이미지 파일을 넣어주세요.')
            return redirect('index')
    
def proceed(request) :
    value = request.GET.get('value')
    data = json.loads(unquote(value))
    
    return render(request, 'cheese/result.html', {'data': data})