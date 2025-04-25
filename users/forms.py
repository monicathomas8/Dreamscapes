from django import forms
from django.contrib.auth.models import User
from .models import CustomOrder


class SignupForm(forms.ModelForm):
    """
    Form for user signup.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Hides password input
        }


class CustomOrderForm(forms.ModelForm):
    """
    Form for creating a custom order.
    """
    class Meta:
        model = CustomOrder
        fields = [
            'description',
            'size',
            'colours',
            'theme',
            'style',
            'extra_suggestions',
            'contact_email',
        ]
