from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('reserve/<int:hotel_id>/', views.reserve_hotel, name='reserve_hotel'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
]
