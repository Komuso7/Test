from django.urls import path
from . import views

urlpatterns = [
    path('Keirsi_Test', views.Keirsi_main, name='Keirsi_Test'),
    path('Keirsi_questions', views.Keirsi_questions, name='questions'),
    path('Keirsi_answer', views.Keirsi_answer, name='Keirsi_answer'),
    path('motivation_Test', views.motivation_main, name='motivation_Test'),
    path('motivation_questions', views.motivation_questions, name='motivation_questions'),
    path('motivation_answer', views.motivation_answer, name='motivation_answer'),
    path('Tomas_Test', views.Tomas_main, name='Tomas_Test'),
    path('Tomas_questions', views.Tomas_questions, name='Tomas_questions'),
    path('Tomas_answer', views.Tomas_answer, name='Tomas_answer')
]

