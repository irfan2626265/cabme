from django.urls import path
from ride.views import UserRideView


urlpatterns = [
    
    path('ride/',UserRideView.as_view(),name='ride'),
]