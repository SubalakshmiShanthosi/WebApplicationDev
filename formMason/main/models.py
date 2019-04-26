from __future__ import unicode_literals
from django.db import models
from jsonfield import JSONField
# Create your models here.


# Creation of one database field  title
class FormSchema(models.Model):
    title=models.CharField(max_length=100)
    schema=JSONField()
