from django import forms

from Hotelio.models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['hotel', 'check_in', 'check_out', 'guests']


class ReviewForm(forms.Form):
    reservation_id = forms.IntegerField(widget=forms.HiddenInput)
    review_text = forms.CharField(
        label="Opinia",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=True
    )
    rating = forms.IntegerField(
        label="Ocena (1-5)",
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=1,
        max_value=5,
        required=True
    )
