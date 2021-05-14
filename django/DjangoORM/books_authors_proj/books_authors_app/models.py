from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    fname = models.CharField(max_length=55)
    lname = models.CharField(max_length=55)
    notes = models.TextField(null=True)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)