from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.MainView.as_view(), name='MainView'),
    path('about', views.AboutView.as_view(), name='about_view'),
    path('call/back/form', views.CallBackFormView.as_view(), name='call_back_form'),
]
