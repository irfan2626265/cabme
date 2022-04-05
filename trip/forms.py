from django.forms import ModelForm
from trip.models import TripModel


class TripForm(ModelForm):
    class Meta:
        model  = TripModel
        exclude = ('status','create_on','update_on',)