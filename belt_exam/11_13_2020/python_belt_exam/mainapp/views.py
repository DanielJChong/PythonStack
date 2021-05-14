from django.shortcuts import render, redirect
from .models import User, Trip
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, "index.html")

def register(request):
    errs = User.objects.register_validator(request.POST)
    if len(errs) > 0:
        for msg in errs.values():
            messages.error(request, msg)
        return redirect('/')
    password = request.POST['password']
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(
        fname=request.POST['fname'],
        lname=request.POST['lname'],
        email=request.POST['email'],
        password=hashed,
    )
    request.session['user_id'] = new_user.id
    return redirect('/success')

def login(request):
    errs = User.objects.login_validator(request.POST)
    if len(errs) > 0:
        for msg in errs.values():
            messages.error(request, msg)
        return redirect('/')
    user_list = User.objects.filter(email=request.POST['email'])
    if user_list:
        our_user = user_list[0]
        if bcrypt.checkpw(request.POST['password'].encode(), our_user.password.encode()):
            request.session['user_id'] = our_user.id
            return redirect('/success')
        else:
            messages.error(request, "User not found, or passwords don't match!")
    else:
        messages.error(request, "User not found, or passwords don't match!")
    return redirect('/')

def success(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    all_trip = Trip.objects.all()
    context = {
        'logged_in_user': logged_in_user,
        'trips': all_trip,
    }
    return render(request, "dashboard.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')


def create_trip(request):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    context = {
        'logged_in_user': logged_in_user,
        'all_trips': Trip.objects.all()
    }
    return render(request, "newtrip.html", context)

def process_trip(request):
    errs = Trip.objects.basic_validator(request.POST)
    if len(errs) > 0:
        for msg in errs.values():
            messages.error(request, msg)
        return redirect('/trips/create')
    logged_in_user = User.objects.get(id=request.session['user_id'])
    new_trip = Trip.objects.create(
        destination=request.POST['destination'],
        sdate=request.POST['sdate'],
        edate=request.POST['edate'],
        plan=request.POST['plan'],
        user=logged_in_user,
    )
    return redirect('/success')

def trip_info(request, trip_id):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=trip_id)
    context = {
        'logged_in_user': logged_in_user,
        'trip': this_trip
    }
    return render(request,"tripinfo.html", context)

def delete_trip(request, trip_id):
    this_trip = Trip.objects.get(id=trip_id)
    this_trip.delete()
    return redirect('/success')

def edit_trip(request, trip_id):
    logged_in_user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=trip_id)
    context = {
        'logged_in_user': logged_in_user,
        'trip': this_trip
    }
    return render(request, "edittrip.html", context)

def process_edit(request, trip_id):
    errs = Trip.objects.basic_validator(request.POST)
    if len(errs) > 0:
        for msg in errs.values():
            messages.error(request, msg)
        return redirect(f'/trips/edit/{trip_id}')
    logged_in_user = User.objects.get(id=request.session['user_id'])
    edit_trip = Trip.objects.get(id=trip_id)
    edit_trip.destination=request.POST['destination']
    edit_trip.sdate=request.POST['sdate']
    edit_trip.edate=request.POST['edate']
    edit_trip.plan=request.POST['plan']
    edit_trip.user=logged_in_user
    edit_trip.save()
    return redirect('/success')