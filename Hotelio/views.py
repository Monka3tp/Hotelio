from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Hotel, Reservation, Review
from .forms import ReservationForm, ReviewForm

def home(request):
    hotels = Hotel.objects.all()
    return render(request, 'home.html', {'hotels': hotels})

def hotel_details(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    reviews = Review.objects.filter(hotel=hotel)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.hotel = hotel
            review.save()
            return redirect('hotel-details', pk=hotel.pk)
    else:
        form = ReviewForm()
    return render(request, 'hotel_details.html', {'hotel': hotel, 'reviews': reviews, 'form': form})

@login_required
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('profile')
    else:
        form = ReservationForm()
    return render(request, 'make_reservation.html', {'form': form})