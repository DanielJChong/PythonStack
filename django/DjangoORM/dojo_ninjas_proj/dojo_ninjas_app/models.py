from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=55)
    # desc = models.TextField(default="old dojo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ninjas = all ninjas within this dojo

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    fname = models.CharField(max_length=55)
    lname = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
