import folium
from branca.element import Figure

from farm.models import Farm, Tour
from func.tour_board import *

def get_farm(id) :
    name = Farm.objects.get(id=id).name
    story = Farm.objects.get(id=id).story
    special = Farm.objects.get(id=id).special
    url = Farm.objects.get(id=id).url
    link = Farm.objects.get(id=id).link
    address = Farm.objects.get(id=id).address
    coord = Farm.objects.get(id=id).coord[1:-1].split(', ')

    map = folium.Map(location=coord, zoom_start=15, width=500, height=300)
    fig = Figure(width=1200, height=300)
    fig.add_child(map)

    text = f'<h4>{name}</h4><h5>{address}</h5>'
    popup = folium.Popup(text, min_width=50, max_width=200)
    folium.Marker(location=coord, popup=popup).add_to(map)
    
    return {'name': name, 'story': story, 'special': special, 'url': url, 'link': link, 'map' :map._repr_html_()}

def get_tour(id) :
    name = Tour.objects.get(id=id).name
    code = Tour.objects.get(id=id).code

    if id == 1 :
        lst = ['와우목장', '은아목장']
    elif id == 2 :
        lst = ['하늘목장']
    else :
        lst = ['파도목장']

    if len(lst) != 1 :
        coord = [37.17228853530072, 127.57083123672544]
        map = folium.Map(location=coord, zoom_start=11, width=500, height=300)
    else :
        coord = Farm.objects.get(name=lst[0]).coord[1:-1].split(', ')
        map = folium.Map(location=coord, zoom_start=15, width=500, height=300)

    fig = Figure(width=1200, height=300)
    fig.add_child(map)

    for l in lst :
        farm = Farm.objects.get(name=l).name
        address = Farm.objects.get(name=l).address
        loc = Farm.objects.get(name=l).coord[1:-1].split(', ')
        text = f'<h4>{farm}</h4><h5>{address}</h5>'
        popup = folium.Popup(text, min_width=50, max_width=200)
        folium.Marker(location=loc, popup=popup).add_to(map)

    review, review_photo, review_reply = get_review(id)
    question, question_photo, question_reply = get_question(id)
    content = {
        'id': id, 'name': name, 'code': code, 'map' :map._repr_html_(),
        'review': review, 'review_photo': review_photo, 'review_reply': review_reply,
        'question': question, 'question_photo': question_photo, 'question_reply': question_reply
        }

    return content