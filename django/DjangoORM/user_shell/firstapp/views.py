from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.

def index(request):
    print(User.objects.all())
    context = {
        'all_user': User.objects.all()
    }
    return render(request, 'index.html', context)  

def process(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    age = request.POST['age']
    User.objects.create(
        fname=fname, 
        lname=lname,
        email=email,
        age=age,
        )
    return redirect('/')