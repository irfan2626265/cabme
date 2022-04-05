from django.urls import path
from vehicle.views import UserVehicleType 

urlpatterns = [
    path('vehicle/',UserVehicleType.as_view(),name='vehicle')
]