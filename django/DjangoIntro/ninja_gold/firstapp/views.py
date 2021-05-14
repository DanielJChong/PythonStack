from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
    if "num" not in request.session:
        request.session["num"] = 0
    if "activity" not in request.session:
        request.session["activity"] = []
    return render(request, "index.html")

def process_money(request):
    if request.POST['gold_source'] == 'farm':
        gold = random.randint(10, 20)
        request.session["num"] += gold
        request.session["activity"].append(f"Got {gold} gold from farm!") 
        print(gold)
        print(request.session["num"])

    if request.POST['gold_source'] == 'cave':
        gold = random.randint(5, 10)
        request.session["num"] += gold
        request.session["activity"].append(f"Got {gold} gold from cave!")
        print(gold)
        print(request.session["num"])

    if request.POST['gold_source'] == 'house':
        gold = random.randint(2, 5)
        request.session["num"] += gold
        request.session["activity"].append(f"Got {gold} gold from house!")
        print(gold)
        print(request.session["num"])

    if request.POST['gold_source'] == 'casino':
        gold = random.randint(-50, 50)
        request.session["num"] += gold
        request.session["activity"].append(f"Got {gold} gold from casino!")
        print(gold)
        print(request.session["num"])

    return redirect('/')