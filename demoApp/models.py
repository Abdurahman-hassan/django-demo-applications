from django.db import models


# Create your models here.

class MenuCategory(models.Model):
    """Model representing a menu category."""
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Menu(models.Model):
    """Model representing a dish in the menu."""
    dish_name = models.CharField(max_length=80)
    dish_description = models.TextField()
    dish_prices = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory,
                                    on_delete=models.PROTECT,
                                    default=None,
                                    related_name='menu_category')
    # dish_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.dish_name + " : " + self.dish_description + " -> " + str(self.dish_prices)