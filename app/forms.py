from .models import StartA
from django.forms import ModelForm, TextInput


class StartAForm(ModelForm):
    class Meta:
        model = StartA
        fields = ["start"]
        widgets = {
            "start": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter URL'
            })
        }
