from django.contrib.auth.models import User
from django.utils import timezone

from farm.models import Reservation, Payment

def get_username(email) :
    if email != 'admin@mail.com' :
        result = User.objects.filter(email=email).all()
        if len(result) != 0 :
            return result[0].username
        
    return None

def check_email(username, email) :
    if username != 'admin' and email != 'admin@mail.com' :
        result = User.objects.filter(email=email).all()
        if len(result) != 0 :
            return email == result[0].email
    
    return False

def get_reservation(user) :
    result = Reservation.objects.filter(user=user).all()
    return result

def get_reservation_id(id) :
    result = Reservation.objects.get(id=id)
    return result

def get_reservation_nonmember(email) :
    return Reservation.objects.filter(email=email).all()

def remove_reservation(id) :
    reservation = Reservation.objects.get(id=id)
    reservation.delete()

def proceed_payment(id, uid, imp_uid, amount) :
    reservation = Reservation.objects.get(id=id)
    settlement = Payment(reservation=reservation, uid=uid, imp_uid=imp_uid, amount=amount)
    reservation.paid_date = timezone.now()
    settlement.save()
    reservation.save()

def cancel_payment(reservate) :
    if Payment.objects.filter(reservation=reservate).all() :
        Payment.objects.get(reservation=reservate).delete()