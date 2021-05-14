from django.shortcuts import render, redirect
from .models import Show

# Create your views here.

def index(request):
    return redirect('/show')

def shows(request):
    all_show = Show.objects.all()
    context = {
        'shows': all_show
    }
    return render(request, "all_shows.html", context)

def edit(request, show_id):
    this_show = Show.objects.get(id=show_id)
    context = {
        'show': this_show
    }
    return render(request, "edit.html", context)

def edit_show(request, show_id):
    edit_show = Show.objects.get(id=show_id)
    edit_show.title=request.POST['title']
    edit_show.network=request.POST['network']
    edit_show.rel_date=request.POST['rel_date']
    edit_show.desc=request.POST['desc']
    edit_show.save()
    return redirect(f'/show/info/{edit_show.id}')


def destroy(request, show_id):
    this_show = Show.objects.get(id=show_id)
    this_show.delete()
    return redirect('/show')

def new_show(request):
    return render(request, "new_show.html")

def process_show(request):
    new_show = Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        rel_date=request.POST['rel_date'],
        desc=request.POST['desc'],
    )
    return redirect(f'/show/info/{new_show.id}')

def show_info(request, show_id):
    this_show = Show.objects.get(id=show_id)
    context = {
        'show': this_show
    }
    return render(request, "show_info.html", context)

