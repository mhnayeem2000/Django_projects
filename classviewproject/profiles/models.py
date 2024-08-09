from django.db import models
from author.models import author
# Create your models here.
class profiles(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField()
    author =  models.ForeignKey(author, on_delete= models.CASCADE)

    def __str__(self):
        return self.name