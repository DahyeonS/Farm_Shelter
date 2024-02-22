from django import forms
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from farm.models import Reservation

# 치즈 예측
class CheeseForm(forms.Form) :
    saveFile = forms.ImageField()

# 회원
class RegisterForm(UserCreationForm) :
    email = forms.EmailField(label='이메일')
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)
    
    class Meta :
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'last_name', 'first_name', 'email')

class ModifyForm(UserChangeForm) :
    email = forms.EmailField(error_messages={'required' : '이메일은 필수로 입력해야 합니다.'})

    class Meta :
        model = get_user_model()
        fields = ('last_name', 'first_name', 'email')

# 예약
class ReservateForm(forms.ModelForm) :
    class Meta :
        model = Reservation
        fields = ['last_name', 'first_name', 'people', 'email', 'password']

    def save(self, commit=True, *args, **kwargs):
        # 추가적인 동작 수행
        # 예: 모델의 save 메서드 호출
        instance = super().save(commit=False, *args, **kwargs)

        # 현재 시각
        current_time = timezone.now()

        # modified_date가 None이 아니고 7일 이상 지났거나 modified_date가 없는 경우
        if instance.modified_date and (current_time - instance.modified_date).days > 7:
            if commit:
                instance.delete()  # 데이터 삭제
            return instance

        # reserved_date가 7일 이상 지났고 paid_date가 None인 경우 행 삭제
        if instance.reserved_date and (current_time - instance.reserved_date).days > 7 and instance.paid_date is None:
            if commit:
                instance.delete()  # 데이터 삭제
            return instance

        # 모델의 save 메서드 호출
        if commit:
            instance.save()
        return instance
    
class ReservationCheck(forms.ModelForm) :
    class Meta :
        model = Reservation
        fields = ['email', 'password']