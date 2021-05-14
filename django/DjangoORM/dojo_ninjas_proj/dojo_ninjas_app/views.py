from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    print(Dojo.objects.all())
    print(Ninja.objects.all())
    context = {
        'all_dojo': Dojo.objects.all(),
        'all_ninja': Ninja.objects.all(),
    }
    return render(request, "index.html", context)

def add_dojo(request):
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    Dojo.objects.create(
        name=name,
        city=city,
        state=state,
    )
    return redirect('/')

def add_ninja(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    dojo = Dojo.objects.get(name=(request.POST["dojo"]))
    Ninja.objects.create(
        fname=fname,
        lname=lname,
        dojo=dojo,
    )
    return redirect('/')