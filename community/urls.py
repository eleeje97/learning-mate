from django.urls import path
from . import views


app_name = 'community'

urlpatterns = [
    path('', views.notice, name='notice'),
    path('notice/', views.notice, name='notice'),
    path('information/', views.information, name='information'),
    path('chat/', views.chat, name='chat'),
    path('community/<int:question_id>/', views.community_detail, name='community_detail'),
    path('information/<int:question_id>/', views.information_detail, name='information_detail'),
    path('notice/<int:question_id>/', views.notice_detail, name='notice_detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('notice/create/', views.notice_create, name='notice_create'),
    path('information/create/', views.information_create, name='information_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('information/delete/<int:question_id>/', views.information_delete, name='information_delete'),
    path('notice/delete/<int:question_id>/', views.notice_delete, name='notice_delete'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify')

]

