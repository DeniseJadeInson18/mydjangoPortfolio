from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'midtermportfolio/index.html')

def galary(request):
    return render(request, 'midtermportfolio/portfolio.html')