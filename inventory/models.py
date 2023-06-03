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
    
    def cost_of_items(self): # made for purchases sake
        ingredients = RecipeRequirement.objects.filter(recipe=self)
        # go to the Receipe Requirements table.grab all of the recipe requiement data attributes. through .objects method. 
        # using.filter we tell python to only give me the objects when they equal this recipe. 
        # recipe is an attribute in the RecipeRequirement table line 44 see below.
        # when that recipe field is equal to self grab the items that were used in making the recipe. 
        # self is an instance of an object. and that was 
        # when this item is equal to the one listed in the recipe grab this value. 


        # we need to access the ingredient cost and add it up. price per unit by the amount used and add it up.
        

        #find me all of the recipe items you need to make this receipe. 
        #self is an instnace of the object. 
        #django djaffe cake as a menu item with descriptiona nd price. we pass that object in and say give me the recipe requirement
        # is this object. 


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
    menu_order = models.ForeignKey(MenuItem,on_delete=models.CASCADE) # this will let us see what menu items were ordered. # without the str method its an object method that you can use for calculations for purchases
    timestamp = models.DateTimeField()

# menu order points to a row on the menu item table 
# menu item is a table with a primary key called id. 
# python will grab the menu item as an object and all of its data.
# menu order is a column in purchases that will have the menu item id in it. 
# django djaffa cake has one id number. and if coffee has an id of two. it will find things by id number. 
# each recipe has an id number of its own. on line 33 of models.py 
# its saying follow those id numbers.


    class Meta:
        verbose_name = "Purchase"


# ask myself what does this table need information for
# what questions am I trying to answer for my boss or for my project?
# when inside of virtual enviornment just run python 
# python manage.py 