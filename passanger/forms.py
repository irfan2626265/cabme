from django.forms import ModelForm
from passanger.models import TripHistoryModel

class TripHistoryForm(ModelForm):
    model = TripHistoryModel
    fields =['__all__']