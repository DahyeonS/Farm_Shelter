from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import base_views, cheese_views, farm_views, reset_views
from .views import ajax_views, tour_views, user_views

urlpatterns = [
    # base
    path('', base_views.index, name='index'),

    # cheese
    path('cheese/list', cheese_views.cheese_list, name='cheese'),
    path('cheese/result', cheese_views.result),
    path('cheese/proceed', cheese_views.proceed),
    path('cheese/detail/<int:id>', cheese_views.detail),

    # farm
    path('farm/list', farm_views.farm_list, name='farm'),
    path('farm/map', farm_views.map, name='map'),
    path('farm/detail/<int:id>', farm_views.detail),

    # tour
    path('tour/list', tour_views.tour_list, name='tour'),
    path('tour/detail/<int:id>', tour_views.detail, name='tour_detail'),
    path('tour/reservate/<int:id>', tour_views.reservate),
    path('tour/payment/<int:id>', tour_views.payment, name='payment'),
    path('tour/payment_result/<int:id>', tour_views.payment_result),

    # user
    path('user/login', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('user/logout', user_views.logout_view, name='logout'),
    path('user/register', user_views.register, name='register'),
    path('user/confirm_password', user_views.confirm_password, name='check_password'),
    path('user/nonmember', user_views.nonmember, name='nonmember'),
    path('user/reservation', user_views.reservation, name='reservation'),
    path('user/modify_reservation/<int:id>', user_views.modify_reservation),
    path('user/delete_reservation/<int:id>', user_views.delete_reservation),
    path('user/modify', user_views.modify, name='modify'),
    path('user/modify_password', user_views.modify_password),
    path('user/search_username', user_views.search_username),
    path('user/delete', user_views.delete, name='delete'),

    # reset
    path('password_reset', reset_views.UserPasswordResetView.as_view()),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/set_password.html'), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/set_password_done.html'), name="password_reset_complete"),

    # ajax
    path('ajax/cheeseResult', ajax_views.cheese_result),
    path('ajax/cheesePaging', ajax_views.cheese_paging),
    path('ajax/farmPaging', ajax_views.farm_paging),
    path('ajax/cheeseSubject', ajax_views.cheese_subject),
    path('ajax/writeReview', ajax_views.write_review),
    path('ajax/updateReview', ajax_views.update_review),
    path('ajax/deleteReview', ajax_views.delete_review),
    path('ajax/reviewReply', ajax_views.review_reply),
    path('ajax/writeReviewReply', ajax_views.write_review_reply),
    path('ajax/updateReviewReply', ajax_views.update_review_reply),
    path('ajax/deleteReviewReply', ajax_views.delete_review_reply),
    path('ajax/writeQuestion', ajax_views.write_question),
    path('ajax/updateQuestion', ajax_views.update_question),
    path('ajax/deleteQuestion', ajax_views.delete_question),
    path('ajax/questionReply', ajax_views.question_reply),
    path('ajax/writeQuestionReply', ajax_views.write_question_reply),
    path('ajax/updateQuestionReply', ajax_views.update_question_reply),
    path('ajax/deleteQuestionReply', ajax_views.delete_question_reply),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)