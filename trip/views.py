from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from trip.models import TripModel
from trip.forms import TripForm

class TripsListView(ListView):
    template_name = 'trips/trip.html'
    model=  TripModel


class TripsCreateView(CreateView):
    template_name = 'trips/create_trip.html'
    success_url = '/trip/'
    form_class= TripForm

class TripsUpdateView(UpdateView):
    template_name = 'trips/create_trip.html'
    model=  TripModel
    fields = '__all__'
    success_url = '/trip/'


class TripsDetailsView(DetailView):
    template_name = 'trips/trip_update.html'
    model=  TripModel
    success_url = '/trip/'


class TripsDeleteView(DeleteView):
    template_name = 'trips/trip_delete.html'
    model=  TripModel
    success_url = '/trip/'



