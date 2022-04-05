from django.db import models
# from trip.models import TripModel

class TripModel(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    # booking_date =models.DateTimeField()
    # cab_no= models.ForeignKey(User,on_delete=models.CASCADE)
    
    # status = models.BooleanField(default=True)
    # create_on = models.DateTimeField(auto_now_add=True)
    # update_on  = models.DateTimeField(auto_now=True)

    
    def __str__(self) -> str:
        return 