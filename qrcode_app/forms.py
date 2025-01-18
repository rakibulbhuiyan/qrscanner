
from django import forms
from .models import CardForm
class CardFormModel(forms.ModelForm):
    class Meta:
        model = CardForm
        fields = ['name', 'phone', 'email', 'location', 'review_link']
        widgets = {
            'review_link': forms.URLInput(attrs={'placeholder': 'Paste your review link here'}),
        }
