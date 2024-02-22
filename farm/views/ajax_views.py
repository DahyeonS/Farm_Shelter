from django.http import JsonResponse

from func.paging import *
from func.tour_board import *

# Create your views here.
def cheese_result(request) :
    cheeses = request.GET.getlist('cheeseKey[]', None)
    result = get_cheese_info(cheeses)
    
    return JsonResponse(result)

def cheese_paging(request) :
    page = request.GET.get('page')
    result = get_cheeses(page)

    return JsonResponse(result)

def farm_paging(request) :
    page = request.GET.get('page')
    result = get_farms(page)

    return JsonResponse(result)

def cheese_subject(request) :
    subject = request.GET.get('sub')
    result = get_name_cheeses(subject)

    return JsonResponse(result, safe=False)

def write_review(request) :
    user = request.user
    tour_id = request.POST.get('tour_id')
    content = request.POST.get('content')
    photo_list = request.FILES.getlist('photo')
    rate = request.POST.get('rate')

    create_review(user, tour_id, content, photo_list, rate)
    return JsonResponse({'rs': 1}, safe=False)

def update_review(request) :
    id = request.POST.get('id')
    content = request.POST.get('content')
    photo_list = request.FILES.getlist('photo')
    rate = request.POST.get('rate')
    file_delete = request.POST.get('fileDelete')

    modify_review(id, content, photo_list, rate, file_delete)
    return JsonResponse({'rs': 1}, safe=False)

def delete_review(request) :
    id = request.POST.get('id')
    remove_review(id)

    return JsonResponse({'rs': 1}, safe=False)

def review_reply(request) :
    id = request.GET.get('id')
    result = get_review_reply(id)
    
    return JsonResponse(result)

def write_review_reply(request) :
    user = request.user
    review_id = request.POST.get('review_id')
    content = request.POST.get('content')

    create_review_reply(user, review_id, content)
    return JsonResponse({'rs': 1}, safe=False)

def update_review_reply(request) :
    id = request.POST.get('id')
    content = request.POST.get('content')

    modify_review_reply(id, content)
    return JsonResponse({'rs': 1}, safe=False)

def delete_review_reply(request) :
    id = request.POST.get('id')
    remove_review_reply(id)

    return JsonResponse({'rs': 1}, safe=False)

def write_question(request) :
    user = request.user
    tour_id = request.POST.get('tour_id')
    content = request.POST.get('content')
    photo_list = request.FILES.getlist('photo')

    create_question(user, tour_id, content, photo_list)
    return JsonResponse({'rs': 1}, safe=False)

def update_question(request) :
    id = request.POST.get('id')
    content = request.POST.get('content')
    photo_list = request.FILES.getlist('photo')
    file_delete = request.POST.get('fileDelete')

    modify_question(id, content, photo_list, file_delete)
    return JsonResponse({'rs': 1}, safe=False)

def delete_question(request) :
    id = request.POST.get('id')
    remove_question(id)

    return JsonResponse({'rs': 1}, safe=False)

def question_reply(request) :
    id = request.GET.get('id')
    result = get_question_reply(id)
    
    return JsonResponse(result)

def write_question_reply(request) :
    user = request.user
    question_id = request.POST.get('question_id')
    content = request.POST.get('content')

    create_question_reply(user, question_id, content)
    return JsonResponse({'rs': 1}, safe=False)

def update_question_reply(request) :
    id = request.POST.get('id')
    content = request.POST.get('content')

    modify_question_reply(id, content)
    return JsonResponse({'rs': 1}, safe=False)

def delete_question_reply(request) :
    id = request.POST.get('id')
    remove_question_reply(id)

    return JsonResponse({'rs': 1}, safe=False)