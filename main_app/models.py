from email import message
from unicodedata import name
from django.db import models
from django.urls import reverse

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'room_id': self.id})


class Chat(models.Model):
    name = models.CharField(max_length=30)
    message = models.TextField(max_length=500)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
