from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_form_view, name='card_form'),
    path('generate-qr/', views.generate_qr, name='generate_qr'),


    path('card-form/', views.card_form_view, name='card_form'),
    path('youtube-video/', views.youtube_video_view, name='youtube_video'),
]
