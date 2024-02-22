import os, json
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from farm.models import Tour, Payment
from farm.forms import ReservateForm
from func.farm_map import get_tour
from func.tour_board import *
from func.user_manage import get_reservation_id, proceed_payment
from func.reserve_mail import reservation_confirm, payment_confirm

# Create your views here.
def tour_list(request) :
    tour = Tour.objects.all()
    return render(request, 'tour/tour_list.html', {'tour': tour})

def detail(request, id) :
    content = get_tour(id)
    return render(request, 'tour/tour.html', content)

def reservate(request, id) :
    if request.method == 'POST' :
        form = ReservateForm(request.POST)
        if form.is_valid() :
            reservate = form.save(commit=False)

            if id == 1 :
                code = 'icheon'
            elif id == 2 :
                code = 'taebaek'
            else :
                code = 'ocean'

            date = str(timezone.now().year) + str(timezone.now().month) + str(timezone.now().day) \
            + str(timezone.now().hour) + str(timezone.now().minute) + str(timezone.now().second)

            if not request.user.username :
                reservate.password = make_password(reservate.password)
            else :
                reservate.user = request.user
                reservate.email = None
                reservate.password = None

            reservate.num = code + request.user.username + date
            reservate.tour = Tour.objects.get(id=id)
            reservate.save()

            reservation_confirm(reservate)
            messages.success(request, '예약이 완료되었습니다. 자세한 내용은 메일로 안내드릴 예정입니다.')
            return redirect('payment', id=reservate.id)
    else :
        form = ReservateForm()

    return render(request, 'tour/reserve.html', {'form': form})

def payment(request, id) : 
    if request.method == 'POST' :
        uid = request.POST.get('uid')
        imp_uid = request.POST.get('impUid')
        amount = request.POST.get('amount')

        proceed_payment(id, uid, imp_uid, amount)
        return JsonResponse({'rs': 1}, safe=False)
    else :
        secret_file = os.path.join('secrets.json')
        with open(secret_file) as f:
            secrets = json.loads(f.read())

        reservation = get_reservation_id(id)
        return render(request, 'tour/payment.html', {'reservation': reservation, 'IMP_CODE': secrets['IMP_CODE']})

def payment_result(request, id) :
    settlement = Payment.objects.get(reservation_id=id)
    payment_confirm(settlement)
    return render(request, 'tour/payment_result.html', {'uid': settlement.uid})