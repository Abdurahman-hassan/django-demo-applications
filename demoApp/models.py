from django.db import models


# Create your models here.
class Menu(models.Model):
    dish_name = models.CharField(max_length=100)
    dish_description = models.TextField()
    dish_price = models.IntegerField()
    # dish_image = models.ImageField(upload_to='images/')