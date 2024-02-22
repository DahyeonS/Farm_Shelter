from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from datetime import datetime

def upload_to_func():
    now = str(datetime.now())[:19]
    prefix = now.replace('-', '').replace(' ', '').replace(':', '')

    return prefix + '/'

# Create your models here.
# 치즈
class Cheese(models.Model) :
    subject = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    content = models.TextField()
    other_cheese = models.TextField()

class Cheese_detail(models.Model) :
    subject = models.CharField(max_length=15)
    name = models.TextField()
    story = models.TextField()
    recipe = models.TextField()
    url = models.TextField()

# 목장
class Farm(models.Model) :
    name = models.TextField()
    story = models.TextField()
    special = models.TextField()
    url = models.TextField()
    link = models.TextField()
    address = models.TextField()
    coord = models.TextField()

# 투어
class Tour(models.Model) :
    name = models.TextField()
    code = models.TextField()
    price = models.IntegerField()

class Reservation(models.Model) :
    num = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    email = models.TextField(null=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=10)
    first_name = models.CharField(max_length=5)
    password = models.TextField(null=True)
    people = models.IntegerField()
    reserved_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    paid_date = models.DateTimeField(null=True)

class Payment(models.Model) :
    uid = models.CharField(max_length=100)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    imp_uid = models.CharField(max_length=100)

# 게시물 관련
class Review(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    content = models.TextField()
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(blank=True, null=True)

class Review_photo(models.Model) :
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to=upload_to_func())

class Review_reply(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

class Question(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(blank=True, null=True)

class Question_photo(models.Model) :
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to=upload_to_func())

class Question_reply(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)