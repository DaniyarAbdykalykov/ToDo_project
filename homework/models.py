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
    ('Январь', 'Январь'),
    ('Февраль', 'Февраль'),
    ('Март', 'Март'),
    ('Апрель', 'Апрель'),
    ('Май', 'Май'),
    ('Июнь', 'Июнь'),
    ('Июль', 'Июль'),
    ('Август', 'Август'),
    ('Сентябрь', 'Сентябрь'),
    ('Октябрь', 'Октябрь'),
    ('Ноябрь', 'Ноябрь'),
    ('Декабрь', 'Декабрь')
]

    goal = models.CharField(max_length=250)
    month = models.CharField(max_length=10, choices= MONTHS_CHOICES, default='Январь')
    difficulty = models.PositiveSmallIntegerField()
    reason_for_goal = models.TextField()


# Create your models here.
