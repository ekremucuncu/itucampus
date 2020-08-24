from django.db import models

# Create your models here.


class WPGroup(models.Model):
    name=models.CharField(max_length=128,blank=False)
    number=models.PositiveIntegerField(blank=False)
    bolum=models.CharField(max_length=128,blank=False)
    mail=models.EmailField(max_length=128,blank=False)

    def __str__(self):
        return self.name
