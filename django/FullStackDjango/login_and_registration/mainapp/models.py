from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        if len(post_data['fname']) < 2:
            errors['fname'] = "First name must be 2 characters or more!"
        if len(post_data['lname']) < 2:
            errors['lname'] = "Last name must be 2 characters or more!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be 8 characters or more!"
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm'] = "Passwords don't match!"
        return errors
    def login_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be 8 characters or more!"
        return errors

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    objects = UserManager()

