from django.db import models

# Create your models here.


class PartsInv(models.Model):

    def __str__(self):
        return self.statdate

    statdate = models.DateField(auto_now=True)
    invvalue = models.FloatField()
