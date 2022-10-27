from django.shortcuts import render, redirect

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
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def rooms_index(request):
    rooms = Room.objects.all()
    return render(request, 'rooms/index.html', {'rooms': rooms})


def rooms_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    chat_form = ChatForm()
    return render(request, 'rooms/detail.html', {'room': room, 'chat_form': chat_form})


def add_chat(request, room_id):
    # create the ModelForm using the data in request.POST
    form = ChatForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_chat = form.save(commit=False)
        new_chat.room_id = room_id
        new_chat.save()
    return redirect('detail', room_id=room_id)
