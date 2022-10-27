from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Define the home view
from .models import Room
from .forms import ChatForm


class RoomCreate(CreateView):
    model = Room
    fields = ['name', 'description']
    success_url = '/rooms/'


class RoomUpdate(UpdateView):
    model = Room
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['name', 'description']


class RoomDelete(DeleteView):
    model = Room
    success_url = '/rooms/'


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def rooms_index(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/index.html', {'rooms': rooms})


def rooms_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    chat_form = ChatForm()
    return render(request, 'rooms/detail.html', {'room': room, 'chat_form': chat_form})
