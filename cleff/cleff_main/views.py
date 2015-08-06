from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'main/home_page.html')


def feed(request):
    return render(request, 'main/feed.html')

def something(request):
    if request.POST:
        print(request.POST)
        return redirect('main:feed')