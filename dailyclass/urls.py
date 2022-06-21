from django.urls import path, include
from . import views

from .views import FileDownloadView, question_list, single_question_page, AddQuestionView

app_name = 'dailyclass'

urlpatterns=[
    #path('', views.home, name='home'),
    path('', views.classmaterial),
    path('classmaterial/', views.classmaterial, name='classmaterial'),
    path('download_file/<int:file_id>/', FileDownloadView.as_view(), name='download'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete'),

    path('test/', views.test_view),
    path('question_list/', question_list.as_view(), name='question_list'),
    path('question/<int:qna_id>/', single_question_page.as_view(), name='single_question_page'),
    path('question_form/', AddQuestionView.as_view(), name="question_form"),

    path('question/create/', views.question_create, name='question_create'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
    #path('save_ans/', views.save_ans, name='saveans'),
]