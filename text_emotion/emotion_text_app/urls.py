from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_form_view, name='text_form'),
    path('predicted_emotion/', views.predicted_emotion_view, name='predicted_emotion'),
]
