from django.urls import path
from . import views


# app_name = 'community'

urlpatterns = [
    path('', views.index),
    # path('',views.main),
    # path('notice/',views.notice,name='notice'),
    # path('sharing_information/',views.sharing_information, name='sharing_information'),
    # path('chat/', views.chat, name='chat')

]

