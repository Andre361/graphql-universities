from django.db import models
from django.contrib.postgres.fields import ArrayField


class University(models.Model):
    name = models.CharField(max_length=255, unique=True, primary_key=True)
    country = models.CharField(max_length=56)
    alpha_two_code = models.CharField(max_length=2)
    web_pages = ArrayField(models.TextField())
    domains = ArrayField(models.TextField(unique=True))
    state_province = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Universities"

