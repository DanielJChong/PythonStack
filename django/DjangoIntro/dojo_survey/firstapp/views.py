from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def processing_form_data(request):
    print("Processing form data")
    print(request.POST)
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    return redirect(f'/success/{name}/{location}/{language}/{comment}')

def success(request, name, location, language, comment):
    context = {
        'name': name,
        'location': location,
        'language': language,
        'comment': comment,
    }
    return render(request, "result.html", context)