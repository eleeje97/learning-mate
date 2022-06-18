from django.urls import path
from . import views


app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    # path('notice/',views.notice,name='notice'),
    # path('sharing_information/',views.sharing_information, name='sharing_information'),
    # path('chat/', views.chat, name='chat')
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]

