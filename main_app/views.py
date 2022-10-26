from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
# Define the home view


class Room:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, description):
        self.name = name
        self.description = description


rooms = [
    Room('titans', 'room for seir titans'),
    Room('drew and matt', 'room for friends'),
]


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def rooms_index(request):
    return render(request, 'rooms/index.html', {'rooms': rooms})
