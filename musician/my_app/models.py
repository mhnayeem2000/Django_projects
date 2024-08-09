from django.db import models

# Create your models here.

class musicians(models.Model):
    first_name = models.CharField(max_length= 20 )
    last_name = models.CharField(max_length= 20 )
    email = models.EmailField()
    phone = models.CharField(max_length= 11)
    instrument_type = models.CharField(max_length= 20)

    def __str__(self):
        return self.first_name
    
class album(models.Model):
    alb_name = models.CharField(max_length  = 50)
    musicians = models.ForeignKey(musicians, on_delete= models.CASCADE)
    date = models.DateField()
    rating = models.IntegerField(default= 0)

    def __str__(self):
        return self.alb_name    

