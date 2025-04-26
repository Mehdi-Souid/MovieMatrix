from django import forms
from .models import Rating
from django.contrib.auth.forms import UserCreationForm
from django.utils.html import format_html
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


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = format_html("""
            <ul class="text-muted small">
                <li>At least 8 characters</li>
                <li>Not too similar to your username</li>
                <li>Not a common password</li>
                <li>Can't be entirely numeric</li>
            </ul>
        """)