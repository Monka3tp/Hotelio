from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ReviewForm
from .models import Hotel, Reservation
from django.contrib.auth.decorators import login_required



def hotel_list(request):
    city = request.GET.get('city', '')
    hotels = Hotel.objects.filter(city=city) if city else Hotel.objects.all()
    hotels = hotels.order_by(F('promo').desc(), 'name')

    cities = Hotel.objects.values_list('city', flat=True).distinct()
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels, 'cities': cities})

@login_required
def reserve_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    if request.method == "POST":
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        guests = request.POST['guests']
        Reservation.objects.create(
            hotel=hotel, user=request.user, check_in=check_in, check_out=check_out, guests=guests
        )
        return redirect('hotel_list')
    return render(request, 'hotels/reservation_from.html', {'hotel': hotel})

@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            reservation_id = form.cleaned_data['reservation_id']
            review_text = form.cleaned_data['review_text']
            rating = form.cleaned_data['rating']

            reservation = Reservation.objects.get(id=reservation_id, user=request.user)
            reservation.review_text = review_text
            reservation.rating = rating
            reservation.save()
            return redirect('my_reservations')
    else:
        form = ReviewForm()

    context = {
        'reservations': reservations,
        'form': form,
    }
    return render(request, 'hotels/my_reservations.html', context)

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    reviews = hotel.reservations.exclude(
        user=request.user) if request.user.is_authenticated else hotel.reservations.all()
    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel, 'reviews': reviews})

@login_required
def my_profile(request):
    return render(request, 'hotels/my_profile.html', {'username': request.user.username})