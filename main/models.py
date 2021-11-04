from django.db import models
from django.utils import timezone

class Text(models.Model):
    name = models.CharField(max_length = 50, primary_key = True)
    text = models.TextField()


class Donation(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    uniq_name = models.CharField(max_length = 20)
    amount = models.IntegerField()
    message = models.TextField()
    already_received = models.BooleanField(default = False)
    active = models.BooleanField(default = True)
    time = models.DateTimeField(default = timezone.now)


class Payment(models.Model):
    donation = models.ForeignKey(Donation, on_delete = models.PROTECT)
    done = models.BooleanField(default = False)
    time = models.DateTimeField(default = timezone.now)
    expired = models.DateTimeField()