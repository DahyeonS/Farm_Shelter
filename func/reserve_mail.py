from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from farm.models import Reservation, Payment

def reservate_mail(subject, reservate, cancel) :
    html_message = render_to_string('user/email/reservation_confirm.html', {'reservate': reservate, 'cancel': cancel})
    plain_message = strip_tags(html_message)
    if reservate.user :
        email = reservate.user.email
    else :
        email = reservate.email
    send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [email], html_message=html_message)

def payment_mail(subject, payment, cancel) :
    html_message = render_to_string('user/email/payment_confirm.html', {'payment':payment, 'cancel': cancel})
    plain_message = strip_tags(html_message)
    if payment.reservation.user :
        email = payment.reservation.user.email
    else :
        email = payment.reservation.email
    send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [email], html_message=html_message)

def reservation_confirm(reservate) :
    subject = f'[목장쉼터] {reservate.last_name}{reservate.first_name}님의 예약이 완료되었습니다.'
    reservate_mail(subject, reservate, False)

def reservation_update(reservate) :
    subject = f'[목장쉼터] {reservate.last_name}{reservate.first_name}님의 예약이 변경되었습니다.'
    reservate_mail(subject, reservate, False)

def reservation_cancel(id) :
    reservation = Reservation.objects.get(id=id)
    subject = f'[목장쉼터] {reservation.last_name}{reservation.first_name}님의 예약이 취소되었습니다.'
    reservate_mail(subject, reservation, timezone.now())

def payment_confirm(settlement) :
    subject = '[목장쉼터] 결제가 완료되었습니다.'
    payment_mail(subject, settlement, False)

def cancel_confirm(reservate):
    payment = Payment.objects.get(reservation=reservate)
    subject = '[목장쉼터] 결제가 취소되었습니다.'
    payment_mail(subject, payment, timezone.now())