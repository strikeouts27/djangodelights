from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length = 20)
    quantity = models.FloatField()
    unit = models.CharField()
    price_per_unit = models.FloatField()
    
    def __str__(self): # without the def_str__ method it will not label ingredient by name
        return " " + self.name

class MenuItem(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    price = models.FloatField()

    def __str__(self):
        return self.name

class RecipeRequirement(models.Model):
    # a recipe_id will populate with django here
    ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE) # the ForeignKey will automatically reference the primary key that Django makes for us.
    recipe = models.ForeignKey(MenuItem,on_delete=models.CASCADE) # the table did not have a concept of which ingredients were tied to what recipe. this line of code associates ingredients with reciepes.
    quantity = models.FloatField()

    def __str__(self):
        return self.recipe.name + " " + self.ingredient.name # you can access values outside of the class to name things. this line of code details the recipe name and ingredient

class Purchases(models.Model):
    # a purchase_id_field will populate with django here
    menu_order = models.ForeignKey(MenuItem,on_delete=models.CASCADE) # this will let us see what menu items were ordered.
    timestamp = models.DateTimeField()

    class Meta:
        verbose_name = "Purchase"


# ask myself what does this table need information for
# what questions am I trying to answer for my boss or for my project?
# when inside of virtual enviornment just run python 
# python manage.py 