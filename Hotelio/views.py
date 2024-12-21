from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, Reservation
from django.contrib.auth.decorators import login_required



def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})

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

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'hotels/hotel_detail.html', {'hotel': hotel})