from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hotel/<int:pk>/', views.hotel_details, name='hotel-details'),
    path('reservation/', views.make_reservation, name='make-reservation'),
]
