import os
from django.utils import timezone
from django.conf import settings

from farm.models import Tour, Review, Review_photo, Review_reply
from farm.models import Question, Question_photo, Question_reply

def get_review(id) :
    review_photo = []
    review_reply = []
    review = Review.objects.filter(tour_id=id).all()
    
    if len(review) != 0 :
        for r in review :
            reply = Review_reply.objects.filter(review_id=r.id).all()
            photo = Review_photo.objects.filter(review_id=r.id).all()
            review_reply.append(reply)
            review_photo.append(photo)
    else :
        review = False

    if len(review_reply) == 0 :
        review_reply = False
    
    return review, review_photo, review_reply

def get_question(id) :
    question_photo = []
    question_reply = []
    question = Question.objects.filter(tour_id=id).all()

    if len(question) != 0 :
        for q in question :
            reply = Question_reply.objects.filter(question_id=q.id).all()
            photo = Question_photo.objects.filter(question_id=q.id).all()
            question_reply.append(reply)
            question_photo.append(photo)
    else :
        question = False

    if len(question_reply) == 0 :
        question_reply = False

    return question, question_photo, question_reply

def create_review(user, tour_id, content, photo_list, rate) :
    tour = Tour.objects.get(id=tour_id)
    review = Review(user=user, tour=tour, content=content, rate=rate)
    review.save()

    for photo in photo_list :
        review_photo = Review_photo(review=review, photo=photo)
        review_photo.save()

def create_question(user, tour_id, content, photo_list) :
    tour = Tour.objects.get(id=tour_id)
    question = Question(user=user, tour=tour, content=content)
    question.save()

    for photo in photo_list :
        question_photo = Question_photo(question=question, photo=photo)
        question_photo.save()

def modify_review(id, content, photo_list, rate, file_delete) :
    review = Review.objects.get(id=id)
    review.content = content
    review.rate = rate
    review.modified_date = timezone.now()
    review.save()

    old_photo = Review_photo.objects.filter(review=review).all()
    folder = ''

    if len(photo_list) != 0 :
        if len(old_photo) != 0 :
            folder = str(old_photo[0].photo).split('/')[0]
        for p in old_photo :
            p.delete()

        if folder != '' :
            os.rmdir(os.path.join(settings.MEDIA_ROOT, folder))

        for photo in photo_list :
            review_photo = Review_photo(review=review, photo=photo)
            review_photo.save()
    
    if len(old_photo) != 0 and file_delete == 'on' :
        photos = Review_photo.objects.filter(review=review).all()
        folder = str(photos[0].photo).split('/')[0]

        for p in photos :
            p.delete()

        os.rmdir(os.path.join(settings.MEDIA_ROOT, folder))

def modify_question(id, content, photo_list, file_delete) :
    question = Question.objects.get(id=id)
    question.content = content
    question.modified_date = timezone.now()
    question.save()

    old_photo = Question_photo.objects.filter(question=question).all()
    folder = ''

    if len(photo_list) != 0 :
        if len(old_photo) != 0 :
            folder = str(old_photo[0].photo).split('/')[0]
        for p in old_photo :
            p.delete()

        if folder != '' :
            os.rmdir(os.path.join(settings.MEDIA_ROOT, folder))

        for photo in photo_list :
            question_photo = Question_photo(question=question, photo=photo)
            question_photo.save()
    
    if len(old_photo) != 0 and file_delete == 'on' :
        photos = Question_photo.objects.filter(question=question).all()
        folder = str(photos[0].photo).split('/')[0]

        for p in photos :
            p.delete()
    
        os.rmdir(os.path.join(settings.MEDIA_ROOT, folder))

def remove_review(id) :
    review = Review.objects.get(id=id)
    photos = Review_photo.objects.filter(review=review).all()
    folder = ''

    if len(photos) != 0 :
        folder = str(photos[0].photo).split('/')[0]

    review.delete()

    if folder != '' :
        os.rmdir(os.path.join(settings.MEDIA_ROOT, folder))

def remove_question(id) :
    question = Question.objects.get(id=id)
    photos = Question_photo.objects.filter(question=question).all()
    folder = ''

    if len(photos) != 0 :
        folder = str(photos[0].photo).split('/')[0]

    question.delete()

    if folder != '' :
        os.rmdir(os.path.join(settings.MEDIA_ROOT, folder))

def get_review_reply(id) :
    replies = []
    reply = Review_reply.objects.all()
    for r in reply :
        replies.append({'id':r.id, 'username':r.user.username, 'content':r.content, 'created_date':r.created_date, 'modified_date':r.modified_date, 'review_id':r.review_id})

    return {'reply':replies}

def get_question_reply(id) :
    replies = []
    reply = Question_reply.objects.all()
    for r in reply :
        replies.append({'id':r.id, 'username':r.user.username, 'content':r.content, 'created_date':r.created_date, 'modified_date':r.modified_date, 'question_id':r.question_id})

    return {'reply':replies}

def create_review_reply(user, review_id, content) :
    review = Review.objects.get(id=review_id)
    reply = Review_reply(user=user, review=review, content=content)
    reply.save()

def create_question_reply(user, question_id, content) :
    question = Question.objects.get(id=question_id)
    reply = Question_reply(user=user, question=question, content=content)
    reply.save()

def modify_review_reply(id, content) :
    reply = Review_reply.objects.get(id=id)
    reply.content = content
    reply.modified_date = timezone.now()
    reply.save()

def modify_question_reply(id, content) :
    reply = Question_reply.objects.get(id=id)
    reply.content = content
    reply.modified_date = timezone.now()
    reply.save()

def remove_review_reply(id) :
    reply = Review_reply.objects.get(id=id)
    reply.delete()

def remove_question_reply(id) :
    reply = Question_reply.objects.get(id=id)
    reply.delete()