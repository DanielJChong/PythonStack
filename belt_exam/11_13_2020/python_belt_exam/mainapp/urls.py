from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('trips/create', views.create_trip),
    path('trips/new', views.process_trip),
    path('trips/info/<int:trip_id>', views.trip_info),
    path('trips/remove/<int:trip_id>', views.delete_trip),
    path('trips/edit/<int:trip_id>', views.edit_trip),
    path('process/edit/<int:trip_id>', views.process_edit),
]