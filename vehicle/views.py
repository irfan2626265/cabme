from django.shortcuts import render
from django.views.generic import TemplateView,DetailView


class UserVehicleType(TemplateView):
    template_name = 'vehicle/vehicle_type.html'


