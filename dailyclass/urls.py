from django.urls import path
from . import views

app_name = 'dailyclass'

urlpatterns=[
    path('', views.classmaterial),
    path('classmaterial/', views.classmaterial),
    path('question_form/', views.question_form),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('test/', views.test_view),
    path('question_list/', views.question_list, name='question_list'),
    path('question/<int:qna_id>/', views.single_question_page),
    path('question/create/', views.question_create, name='question_create'),
]