from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    calories = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()

    def _str_(self):
        return self.title

class Records(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cals100 = models.IntegerField()
    protein100 = models.IntegerField()
    fat100 = models.IntegerField()
    carbs100 = models.IntegerField()
    foods100 = models.CharField(max_length=500)

    def _str_(self):
        return self.title