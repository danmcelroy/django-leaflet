from django.forms import ModelForm
from .models import SamplingStation

class SamplingStationForm(ModelForm):
    class Meta:
        model = SamplingStation
        fields = ['title','description','station_type','geom']
