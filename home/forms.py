from django import forms
from .models import ArtistBio, ContactMessage


class ArtistBioForm(forms.ModelForm):
    class Meta:
        model = ArtistBio
        fields = [
            "name",
            "inspiration",
            "background",
            "interests",
            "work_experience",
            "profile_image",
        ]
        widgets = {
            "background": forms.Textarea(attrs={"rows": 4}),
            "interests": forms.Textarea(attrs={"rows": 3}),
            "work_experience": forms.Textarea(attrs={"rows": 3}),
            "inspiration": forms.Textarea(attrs={"rows": 3}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
