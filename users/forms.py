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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'description': 'Describe your custom art request...',
            'size': 'e.g. A4, 30x40cm',
            'colours': 'Preferred colours (e.g. blue, gold)',
            'theme': 'e.g. Mountains at night',
            'style': 'e.g. Minimalist, abstract',
            'extra_suggestions': 'Any other ideas or inspirations',
            'contact_email': 'Your email address',
        }

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = (
                placeholders.get(field_name, '')
            )


class UserUpdateForm(forms.ModelForm):
    """
    Form for updating user profile information.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
