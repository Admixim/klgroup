from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'dist/index.html')

def src(request):
    return render(request, 'src/index.html')

def calendar(request):
    return render(request, 'dist/calendar.html')

