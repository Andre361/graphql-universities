from django.db import models
from django.contrib.postgres.fields import ArrayField

class CharNullField(models.CharField):
    """ charfield that stores null but returns '' """
    def to_python(self,value):
        if isinstance(value,models.CharField):
            return value
        if value == None:
            return ""
        else:
            return value
    def get_db_prep_value(self,value):
        if value=="":
            return None
        else:
            return value

class University(models.Model):
    name = models.TextField()
    country = models.CharField(max_length=56)
    alpha_two_code = models.CharField(max_length=2)
    web_pages = ArrayField(models.TextField())
    domains = ArrayField(models.TextField())
    state_province = models.TextField(null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Universities"
    