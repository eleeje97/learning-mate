from django.urls import path
from . import views
from .views import FileDownloadView

app_name = 'dailyclass'

urlpatterns=[
    path('', views.classmaterial),
    path('classmaterial/', views.classmaterial, name='classmaterial'),
    path('download_file/<int:file_id>/', FileDownloadView.as_view(), name='download'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete'),
    path('question_form/', views.question_form),
    path('test/', views.test_view),
    path('question_list/', views.question_list, name='question_list'),
    path('question/<int:qna_id>/', views.single_question_page),
    path('question/create/', views.question_create, name='question_create'),
]