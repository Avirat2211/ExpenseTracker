from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name