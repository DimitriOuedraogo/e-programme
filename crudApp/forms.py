from django import forms
from .models import Tache, JourSemaine


class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['nom', 'periode']
        periode = forms.ChoiceField(
            choices=Tache.PERIODE_CHOICES,
            widget=forms.Select()
        )
