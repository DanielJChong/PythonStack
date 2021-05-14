from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        'all_books': Book.objects.all(),
    }
    return render(request, "index.html", context) 

def process_book(request):
    Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['desc'],
    )
    return redirect('/')

def book_info(request, book_id):
    this_book = Book.objects.get(id=book_id)
    context = {
        'book': this_book,
        'all_authors': Author.objects.all(),
    }
    return render(request, "book_info.html", context)

def add_author_to_book(request):
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_book.authors.add(this_author)
    return redirect(f'/books/{this_book.id}')


def authors(request):
    context = {
        'all_authors': Author.objects.all(),
    }
    return render(request, "add_author.html", context)

def process_author(request):
    Author.objects.create(
        fname=request.POST['fname'],
        lname=request.POST['lname'],
        notes=request.POST['notes'],
    )
    return redirect('/authors')

def author_info(request, author_id):
    this_author = Author.objects.get(id=author_id)
    context = {
        'author': this_author,
        'all_books': Book.objects.all(),
    }
    return render(request, "author_info.html", context)

def add_book_to_author(request):
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_author.books.add(this_book)
    return redirect(f'/authors/{this_author.id}')