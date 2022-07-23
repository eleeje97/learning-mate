from django.urls import path, include
from . import views
from . import static

from .views import FileDownloadView, question_list, single_question_page, AddQuestionView, UpdateQuestionView, \
    DeleteQuestionView, \
    AddCommentView, DeleteAnswerView, UpdateAnswerView
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView


app_name = 'dailyclass'

urlpatterns=[
    #path('', views.home, name='home'),
    path('', views.classmaterial),
    path('classmaterial/', views.classmaterial, name='classmaterial'),
    path('download_file/<int:file_id>/', FileDownloadView.as_view(), name='download'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete'),


    path('question_list/', question_list.as_view(), name='question_list'),
    path('question/<int:pk>/', single_question_page.as_view(), name='single_question_page'),
    path('question/question_form/', login_required(AddQuestionView.as_view()), name="question_form"),
    path('question/edit/<int:pk>', login_required(UpdateQuestionView.as_view()), name='question_update_form'),
    path('question/edit/<int:pk>/remove', login_required(DeleteQuestionView.as_view()), name='delete_question'),
    path('question/<int:pk>/ans_remove', login_required(DeleteAnswerView.as_view()), name='delete_answer'),
    path('question/<int:pk>/comment/', login_required(AddCommentView.as_view()), name='add_comment'),
    path('question/comment/<int:pk>/edit', login_required(UpdateAnswerView.as_view()), name='edit_comment'),



] #+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)