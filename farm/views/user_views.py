from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from farm.forms import RegisterForm, ModifyForm, ReservateForm, ReservationCheck
from func.user_manage import *
from func.reserve_mail import reservation_update, reservation_cancel, cancel_confirm

# Create your views here.
@login_required(login_url='login')
def logout_view(request) :
    logout(request)
    return redirect('index')

def register(request) :
    if request.method == 'POST' :
        form = RegisterForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('login')
    else :
        form = RegisterForm()

    return render(request, 'user/register.html', {'form': form})

@login_required(login_url='login')
def confirm_password(request) :
    if request.method == 'POST' :
        password = request.POST.get('password')
        if check_password(password, request.user.password) :
            return redirect(request.POST.get('next'))
        else :
            messages.error(request, '비밀번호가 일치하지 않습니다.')

    return render(request, 'user/confirm_password.html')

def nonmember(request) :
    result = []

    if request.method == 'POST' :
        form = ReservationCheck(request.POST)
        if form.is_valid() :
            check = form.cleaned_data
            reserve = get_reservation_nonmember(check['email'])

            if len(reserve) != 0 :
                for r in reserve :
                    if check_password(check['password'], r.password) :
                        result.append(r)

            if len(result) == 0 :
                messages.error(request, '조회된 예약이 없습니다.')
    else :
        form = ReservationCheck()

    if len(result) != 0 :
        return render(request, 'user/reservation_nonmember.html', {"reservation": result})
    else :
        return render(request, 'user/nonmember.html', {"form": form})

def reservation(request) :
    user = request.user
    content = get_reservation(user)

    return render(request, 'user/reservation.html', {'reservation': content})

@login_required(login_url='login')
def modify_reservation(request, id) :
    reservate = get_reservation_id(id)
    raw_fname = reservate.first_name
    raw_name = reservate.last_name
    raw_people = reservate.people

    if request.method == 'POST' :
        form = ReservateForm(request.POST, instance=reservate)
        if form.is_valid() :
            new_reservate = form.save(commit=False)
            new_reservate.email = None
            new_reservate.password = None
            new_reservate.modified_date = timezone.now()
            new_reservate.save()

            if raw_fname != new_reservate.first_name or raw_name != new_reservate.last_name \
            or raw_people != new_reservate.people :
                reservation_update(new_reservate)
                messages.success(request, '예약이 변경되었습니다. 자세한 내용은 메일로 안내드릴 예정입니다.')
            else :
                messages.success(request, '변경된 내용이 없습니다.')

            if raw_people != new_reservate.people :
                cancel_confirm(reservate)
                cancel_payment(reservate)
                new_reservate.paid_date = None
                new_reservate.save()
                return redirect('payment', id=reservate.id)
            
            return redirect('reservation')

    else :
        form = ReservateForm(instance=reservate)

    return render(request, 'user/modify_reservation.html', {'form': form, 'id':id})

@login_required(login_url='login')
def delete_reservation(request, id) :
    if request.user.is_authenticated :
        reservate = get_reservation_id(id)
        cancel_confirm(reservate)
        cancel_payment(reservate)
        reservation_cancel(id)
        remove_reservation(id)
        messages.success(request, '예약이 취소되었습니다.')
    return redirect('reservation')

@login_required(login_url='login')
def modify(request) :
    if request.method == 'POST' :
        form = ModifyForm(request.POST, instance=request.user)
        if form.is_valid() :
            form.save()
            messages.success(request, '회원정보가 성공적으로 변경되었습니다.')
            return redirect('modify')
    else :
        form = ModifyForm(instance=request.user)

    return render(request, 'user/modify.html', {'form': form})

@login_required(login_url='login')
def modify_password(request) :
    if request.method == 'POST' :
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid() :
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
            return redirect('modify')
    else :
        form = PasswordChangeForm(request.user)

    return render(request, 'user/modify_password.html', {'form': form})

def search_username(request) :
    if request.method == 'POST' :
        email = request.POST.get('email')
        username = get_username(email)

        if username :
            messages.success(request, f'아이디가 조회되었습니다. 아이디는 {username}입니다.')
            return redirect('login')
        else :
            messages.error(request, '아이디를 조회하지 못 했습니다.')

    return render(request, 'user/search_username.html')

@login_required(login_url='login')
def delete(request) :
    if request.user.is_authenticated :
        request.user.delete()
        logout(request)
        messages.success(request, '회원탈퇴가 완료되었습니다. 그동안 감사했습니다.')
        return redirect('index')