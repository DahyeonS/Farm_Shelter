from django.core.paginator import Paginator 

from farm.models import Cheese, Cheese_detail, Farm, Tour

def get_cheese_info(cheeses) :
    names = []
    info = []

    cheese = Cheese.objects.get(subject=cheeses[0])
    info.append({'content':cheese.content, 'other_cheese':cheese.other_cheese})

    for c in cheeses :
        data = Cheese.objects.get(subject=c)
        names.append(data.name)

    return {'info':info, 'name':names}

def get_cheeses(page) :
    data = []

    cheeses = Cheese_detail.objects.all()
    paginator = Paginator(cheeses, 8)
    page_obj = paginator.get_page(page)

    for obj in page_obj :
        data.append({'id':obj.id, 'name':obj.name, 'url':obj.url})

    result = {'items':data, 'pageRange':list(page_obj.paginator.page_range)}
    return result

def get_farms(page) :
    data = []

    farms = Farm.objects.all()
    paginator = Paginator(farms, 12)
    page_obj = paginator.get_page(page)

    for obj in page_obj :
        data.append({'id':obj.id, 'name':obj.name, 'url':obj.url})

    result = {'items':data, 'pageRange':list(page_obj.paginator.page_range)}
    return result

def get_name_cheeses(sub) :
    data = []

    cheeses = Cheese_detail.objects.filter(subject=sub)
    for obj in cheeses :
        data.append({'id':obj.id, 'name':obj.name, 'url':obj.url})

    return data