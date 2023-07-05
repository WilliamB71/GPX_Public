from django import forms
from .models import Gpx

class GpxForm(forms.ModelForm):
    class Meta:
        model = Gpx
        fields = ('start_location', 'end_location', 'transport_method')
