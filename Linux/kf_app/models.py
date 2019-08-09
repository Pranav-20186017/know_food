from django.db import models

# Create your models here.
class Vegetable(models.Model):
	veg_name = models.CharField(max_length = 30)
	calories = models.CharField(max_length = 10)
	total_fat = models.CharField(max_length = 10)
	saturated_fat = models.CharField(max_length = 10)
	sodium = models.CharField(max_length = 10)
	total_carbohydrate = models.CharField(max_length = 10)
	fiber = models.CharField(max_length = 10)
	sugar = models.CharField(max_length = 10)
	protein = models.CharField(max_length = 10)
	vitamin_a = models.CharField(max_length = 10)
	vitamin_c = models.CharField(max_length = 10)
	calcium = models.CharField(max_length = 10)
	iron = models.CharField(max_length = 10)
	
class Recipies(models.Model):
	veg_name = models.CharField(max_length = 30)
	name_of_dish = models.CharField(max_length = 50)
	link = models.CharField(max_length = 1000)
	no_of_cals = models.CharField(max_length = 10)