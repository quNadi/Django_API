from django.db import models

class DataSet(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=100)
    set=models.IntegerField(default=100)
