from django.db import models


# Create your models here.
class Stock(models.Model):
    image=models.ImageField(upload_to='images')
    date_generation=models.DateTimeField(auto_now=True)






