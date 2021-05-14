from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('processing_form_data', views.processing_form_data),
    path('success/<name>/<location>/<language>/<comment>', views.success),
]
