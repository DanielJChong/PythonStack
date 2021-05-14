from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

# Create your views here.

def time_display(request):
    context = {
        "date": strftime("%m-%d-%Y", gmtime()),
        "time": strftime("%I:%M:%S %p", gmtime())
    }
    return render(request,'index.html', context)


