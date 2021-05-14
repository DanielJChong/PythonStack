from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('process_book', views.process_book),
    path('books/<int:book_id>', views.book_info),
    path('add_author_to_book', views.add_author_to_book),
    path('authors', views.authors),
    path('process_author', views.process_author),
    path('authors/<int:author_id>', views.author_info),
    path('add_book_to_author', views.add_book_to_author),
]