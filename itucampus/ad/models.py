from django.db import models
from django.contrib.auth.models import User

class Ad(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='ad_author')
    title = models.CharField(max_length=128)
    body = models.CharField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
