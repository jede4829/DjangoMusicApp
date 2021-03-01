from django import forms

from .models import Jelly

class JellyForm(forms.ModelForm):
    class Meta:
        model = Jelly
        fields = [
            'title'
        ]
