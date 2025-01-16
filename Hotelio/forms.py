from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text="Wprowadź swoje imię.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Wprowadź swoje nazwisko.")
    email = forms.EmailField(max_length=254, required=True, help_text="Wprowadź swój adres e-mail.")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user