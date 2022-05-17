from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'dist/include/base.html')

def src(request):
    return render(request, 'src/base.html')

def calendar(request):
    return render(request, 'dist/include/calendar.html')

