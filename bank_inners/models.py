from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    
    def __str__(self):
        return str(self.user)