from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('chatui/', views.chatui, name='chatui'),
]
