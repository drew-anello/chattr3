from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView
# Define the home view
from .models import Room


class RoomCreate(CreateView):
    model = Room
    fields = '__all__'


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def rooms_index(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/index.html', {'rooms': rooms})


def rooms_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    return render(request, 'rooms/detail.html', {'room': room})
