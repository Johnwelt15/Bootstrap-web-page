from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def forPage(request):
    context = {}
    context ['count'] = list(range(1, 11))
    return render(request, 'for.html')
