# from django.db import models
# from drive.models import DriveModel

# from profiles.models import UserProfileModel

# class TripHistoryModel(models.Model):
#     passanger_id = models.ForeignKey(UserProfileModel,on_delete=models.CASCADE)
#     driver_id = models.ForeignKey(DriveModel,on_delete=models.CASCADE)
#     booked_date = models.DateTimeField(auto_now_add=True)
#     Vehicle_no  = models.CharField(max_length=10)
#     status = models.BooleanField(default=True)
#     create_on = models.DateTimeField(auto_now_add=True)
#     update_on  = models.DateTimeField(auto_now=True)
    
#     def __str__(self) -> str:
#         return 