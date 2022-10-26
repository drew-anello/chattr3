from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('rooms/', views.rooms_index, name='index'),
    path('rooms/<int:room_id>/', views.rooms_detail, name='detail'),
]
