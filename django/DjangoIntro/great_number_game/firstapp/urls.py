from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('tooHigh', views.tooHigh),
    path('tooLow', views.tooLow),
    path('correct', views.correct),
    path('reset', views.reset),
]