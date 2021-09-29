from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, blank=False)
    population = models.CharField(max_length=100, blank=False)
    area = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name