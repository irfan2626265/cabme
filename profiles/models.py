from django.db import models
# from django.contrib.auth.models import AbstractUser, Manager
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save

# add AUTH_USER_MODEL = '<path-to-user-model>'

User = get_user_model()

class Profile(models.Model):
    GENDER_CHOICES = [
            ('M','Male'),
            ('F','Female'),
            ('Other','Other')
        ]
    first_name = models.CharField(max_length=100,blank=True,null=True) 
    last_name = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to='image',default='default/user.png')
    age = models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,blank=True,null=True)
    phone = models.CharField(max_length=16,blank=True,null=True)
    house_name = models.CharField(max_length=60,blank=True,null=True)
    place= models.CharField(max_length=60,blank=True,null=True)
    postoffice= models.CharField(max_length=60,blank=True,null=True)
    pincode = models.CharField(max_length=50,blank=True,null=True) 
    district = models.CharField(max_length=50,blank=True,null=True)
    state = models.CharField(max_length=50,blank=True,null=True)
    country = models.CharField(max_length=50,blank=True,null=True)
    status = models.BooleanField(default=True)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on  = models.DateTimeField(auto_now=True)

    


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=20)


def create_profile(sender, instance, **kwargs):
    # if created:
    profile = Profile.objects.create()
    instance.profile = profile

pre_save.connect(create_profile, sender=User)