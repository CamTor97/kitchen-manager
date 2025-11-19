from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    in_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="in stock")
    unit_type = models.CharField(max_length=100, verbose_name="unit type")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="unit price")
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class RecipeRequirement(models.Model):
    recipe = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="requirements")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_needed = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.ingredient.name

class Purchase(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True)