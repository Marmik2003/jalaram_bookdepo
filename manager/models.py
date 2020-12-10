from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PersonalAccount(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_name = models.CharField(max_length=75)
    transaction_amount = models.IntegerField()
    transaction_datetime = models.DateTimeField(auto_now_add=True)
    