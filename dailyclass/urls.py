from django.urls import path, include
#from .views import quiz, result, save_ans
from . import views
app_name = 'dailyclass'

urlpatterns=[
    path('', views.home, name='home'),
    path('classmaterial/', views.classmaterial),
    path('question_form/', views.question_form),
    path('quiz/', views.quiz, name='quiz'),
    #path('result/', views.result, name='result'),
    #path('save_ans/', views.save_ans, name='saveans'),
]