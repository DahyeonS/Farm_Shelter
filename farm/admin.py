from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cheese)
admin.site.register(Farm)
admin.site.register(Cheese_detail)
admin.site.register(Tour)
admin.site.register(Reservation)
admin.site.register(Review_reply)
admin.site.register(Question_reply)

class ReviewPhotoInline(admin.TabularInline):
    model = Review_photo

class ReviewAdmin(admin.ModelAdmin):
    inlines = [ReviewPhotoInline, ]

class QuestionPhotoInline(admin.TabularInline):
    model = Question_photo

class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionPhotoInline, ]

admin.site.register(Review, ReviewAdmin)
admin.site.register(Question, QuestionAdmin)