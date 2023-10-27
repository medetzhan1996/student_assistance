from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('message/create', views.MessageCreateView.as_view(), name='message_create'),
    path('message/delete/<int:pk>', views.MessageDeleteView.as_view(), name='message_delete'),
    path('message/delete/all', views.MessageDeleteView.as_view(), name='message_delete'),
]
