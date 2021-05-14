from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
    randNum = random.randint(1, 100)
    if "num" not in request.session:
        request.session["num"] = randNum
        print(request.session["num"])
    return render(request, "index.html")

def process(request):
    guess = int(request.POST['guess'])
    randNum = request.session['num']
    if guess > randNum:
        return redirect('/tooHigh')
    elif guess < randNum:
        return redirect('/tooLow')
    else: 
        return redirect('/correct')

def tooHigh(request):
    return render(request, "tooHigh.html")

def tooLow(request):
    return render(request, "tooLow.html")

def correct(request):
    return render(request, "correct.html")


def reset(request):
    request.session.clear()
    return redirect('/')
