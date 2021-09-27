from django.db import models

class Windmill(models.Model):

    title = models.CharField(max_length=256)
    windmill_type = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.title
