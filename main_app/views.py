from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from .models import Room
# Define the home view


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def rooms_index(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/index.html', {'rooms': rooms})
