from django.db import models
from django.contrib.auth.models import User
from PIL import Image


## create User model to add e.g. a profile picture (extend existing one)
## one user can have one profile and one profiles can be owned by one user only
class Profile(models.Model):
    ''' on delete - what to do with a Profile when User is deleted
    ## but if we delete a Profile, it will NOT delete a User '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ## have a default image for profiles, store images in 'profile_pics' directory
    image = models.ImageField(default='default.jpg', upload_to='profile__pics')

    ## how we want Profile to be displayed (instead of default "Profile Object"
    def __str__(self):
        return f'{self.user.username} Profile'

    ## override parent class save method so we can resize images
    ## TODO - delete old, unused picture
    def save(self):
        super().save()

        ## open current Profile instance's image
        img =  Image.open(self.image.path)

        ## resize if too big
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)   ## save to the same path