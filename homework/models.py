from django.db import models

class ToMeet(models.Model):
    persone = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date_of_meeting = models.DateTimeField()
    comment = models.TextField(null=True, blank=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


# Create your models here.
