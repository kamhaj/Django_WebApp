'''
django docs recommends to create a separate files for this, instead of putting this code in models.py
we set it up for user profile edition availability

idea behind it is this: if sth happens, make another sth happen (signals, like triggers)
example: if User is created (registered), send signal to create him/her a Profile
'''

from django.db.models.signals import post_save
from django.contrib.auth.models import User     ## User model is going to be a signal sender
from django.dispatch import receiver ## signal receiver (as decorator)
from .models import Profile ## needed, since we'll create Profiles in our function. We need a new Profile for each new User



''' when User is saved then send signal to receiver'''
## receiver function invoked every time User is created
@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):        ## kwargs for any additional arguments
    ## if 'instance' of User was 'created'
    if created:
        Profile.objects.create(user=instance)

@receiver(signal=post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    ## save Profile when User is saved
    instance.profile.save()