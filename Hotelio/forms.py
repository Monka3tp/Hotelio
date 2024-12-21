from django import forms

from Hotelio.models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['hotel', 'start_date', 'end_date', 'guests']

