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
            'password': forms.PasswordInput(),
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


class UserUpdateForm(forms.ModelForm):
    """
    Form for updating user profile information.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
