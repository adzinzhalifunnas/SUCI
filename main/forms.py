from django import forms

class DonationForm(forms.Form):
    name = forms.CharField(max_length = 20)
    email = forms.EmailField()
    message = forms.CharField(max_length = 150)
    total = forms.CharField(max_length = 25)