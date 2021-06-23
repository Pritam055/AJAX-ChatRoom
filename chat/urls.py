from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chatroom/<str:room>/<str:username>/', views.get_chat_room, name='chatroom'),
    path('send-message/', views.get_send_message, name='send-message'),
    path('all-messages/<str:room>/', views.get_all_messages, name='all-messages'),
]