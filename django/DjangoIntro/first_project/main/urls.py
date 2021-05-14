from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('success', views.success),
    path('name/<namey_name>', views.say_hi),
    path('name/<namey_name>/<int:num>', views.say_hi),
    path('index', views.connect),
    path('dragon', views.connect_dic),
    path('redirected', views.redirected_to_home),
]