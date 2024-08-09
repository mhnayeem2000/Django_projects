from django.db import models
from categories.models import category
from author.models import author
# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length = 40)
    description = models.TextField()
    category = models.ManyToManyField(category)
    author = models.ForeignKey(author, on_delete= models.CASCADE)

    def __str__(self):
        return self.title