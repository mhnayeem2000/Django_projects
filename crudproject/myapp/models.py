from django.db import models

# Create your models here.

class update_user(models.Model):
    uid = models.IntegerField()
    name =  models.CharField(max_length= 20)
    department = models.CharField(max_length= 20)
    aim = models.TextField( default=True)
    
    def __str__(self):
        return self.name