from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rev_stars']
        widgets = {
            'rev_stars': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'class': 'form-control'
            })
        }
        labels = {
            'rev_stars': 'Your Rating (1-5 stars)'
        }