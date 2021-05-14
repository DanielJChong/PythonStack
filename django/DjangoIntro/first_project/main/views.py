from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("some string")

def success(request):
    return HttpResponse('You hit the cusccess route!')

def say_hi(request, namey_name):
    return HttpResponse(f'Hi {namey_name}')

def say_hi(request, namey_name, num):
    return HttpResponse(f'Hi {namey_name}' * num)

def connect(request):
    return render(request, 'index.html')

def connect_dic(request):
    dragon = {
        'name': "Johnny",
        "num": 123
    }
    return render(request, 'index.html', dragon)

def redirected_to_home(request):
    print('I am in the redirect.')
    return redirect('/success')