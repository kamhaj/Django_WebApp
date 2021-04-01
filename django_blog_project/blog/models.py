from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


## one (user) to many (posts) relation
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()        # unrestricted text
    date_posted = models.DateTimeField(default=timezone.now)  #its a function now(), but we dont want to execute it right away??
    author = models.ForeignKey(User, on_delete=models.CASCADE) ## if user was deleted, deleted his/her posts as well


    def __str__(self):
        ## return it in a way you want it to be printed out
        return self.title

