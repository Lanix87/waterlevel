from django.db import models

# Create your models here.

class Tower(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=0)
    pump = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Башня'
        verbose_name_plural = 'Башня'

class TowerActivity(models.Model):
    date = models.DateTimeField(default=None)
    is_pumping = models.BooleanField(default=None)

    class Meta:
        verbose_name = 'Історія'
        verbose_name_plural = 'Історія'
