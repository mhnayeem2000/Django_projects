from django.db import models

# Create your models here.

class User(models.Model):
    uid = models.IntegerField(default = 1 ,primary_key=True)
    name = models.CharField(max_length= 20)
    department = models.CharField(max_length= 20)

    def __str__(self):
        return self.name
    

class addusermodel(models.Model):
    uid = models.IntegerField(default = 1 ,primary_key=True)
    name = models.CharField(max_length= 20)
    department = models.CharField(max_length= 20)

