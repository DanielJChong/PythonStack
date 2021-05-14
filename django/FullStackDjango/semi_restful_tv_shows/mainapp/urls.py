from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('show', views.shows),
    path('show/<int:show_id>/edit', views.edit),
    path('show/edit/<int:show_id>', views.edit_show),
    path('shows/<int:show_id>/destroy', views.destroy),
    path('show/create', views.process_show),
    path('show/info/<int:show_id>', views.show_info),
    path('show/new', views.new_show),
]