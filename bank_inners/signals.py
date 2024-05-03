from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

from .models import *

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('Profile created!')

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    print('Profile updated!')
