from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def store(request):
    return render(request, 'store.html')    

def branch(request):
    return render(request, 'branch.html')

def contact(request):
    return render(request, 'contact.html')



def privacy(request):
    return render(request, 'privacy.html')


