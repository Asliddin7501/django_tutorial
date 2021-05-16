from django import forms
from .models import Telefon

class TelefonForm(forms.ModelForm):
    class Meta:
        model = Telefon
        fields = [
            'kompaniya_nomi',
            'rusumi',
            'xotirasi',
            'tezkor_xotirasi',
            'narxi'
        ]