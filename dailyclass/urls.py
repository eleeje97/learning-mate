from django.urls import path
from . import views

app_name = 'dailyclass'

urlpatterns=[
    path('', views.classmaterial),
    path('classmaterial/', views.classmaterial),
    path('question_form/', views.question_form),
    path('test/', views.test_view),
]