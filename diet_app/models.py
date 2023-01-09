from django.db import models

# Create your models here.
class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    dish_id = models.IntegerField()
    dish_name = models.CharField(max_length=250)
    dish_time = models.CharField(max_length=50)
    dish_ingredient = models.CharField(max_length=250)
    ingredient_weight = models.IntegerField()
    ingredient_unit = models.CharField(max_length=10)

    def __str__(self):
        return self.dish_name