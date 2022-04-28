from calendar import month
from statistics import mode
from django.db import models

class ToMeet(models.Model):
    persone = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date_of_meeting = models.DateTimeField()
    comment = models.TextField(null=True, blank=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class Goal_for_month(models.Model):

    MONTHS_CHOICES = [
    ('1', 'Январь'),
    ('2', 'Февраль'),
    ('3', 'Март'),
    ('4', 'Апрель'),
    ('5', 'Май'),
    ('6', 'Июнь'),
    ('7', 'Июль'),
    ('8', 'Август'),
    ('9', 'Сентябрь'),
    ('10', 'Октябрь'),
    ('11', 'Ноябрь'),
    ('12', 'Декабрь')
]

    goal = models.CharField(max_length=250)
    month = models.CharField(max_length=2, choices= MONTHS_CHOICES, default='1')
    difficulty = models.PositiveSmallIntegerField()
    reason_for_goal = models.TextField()


# Create your models here.
