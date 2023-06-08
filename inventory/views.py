from django.shortcuts import render
from django.urls import path 
from .models import Ingredient, MenuItem, Purchases, RecipeRequirement
from django.views.generic import ListView

from django.http import HttpResponse

# Create your views here.

def finance(request):
    purchased_items = Purchases.objects.all() # this grabs every row in the purchases table

    total_revenue = 0 
    for item in purchased_items:
        total_revenue = total_revenue + item.menu_order.price #this uses the price of each item to calculate the revenue
    
    print(str(total_revenue))
    total_cost= ingredient_cost_calculate()
    print(str(total_cost) + " this is the total cost calculation")

    total_profit= total_revenue - total_cost
    print(str(total_profit) + "total profit calculation amount")

    return render(request,'inventory/finance.html', {"total_revenue": total_revenue, "total_cost":total_cost, "total_profit": total_profit})    
    # i want the price of the item and the cost of each item.
    # what holds this information? my ingredient model. 
    # it holds the price per unit and the unit.
def ingredient_cost_calculate(): 
    # classes do not store information objects do. 
    # i need the cost per ingredient multiplied by quantity used.
    # I need to than for loop over all of the ingredients in a recipe and than apply the cost per ingredient function or 
    # the same mathematical operation. 
    # classes do not have the data, the objects do.
    # when the customer purchases something an entry is made in the purchases table. 
    # Purchases.objects.all() grabs all of the Purchases data and puts it in a list.
    purchases_objects = Purchases.objects.all() 
    # I need to find all of the ingredients per order. How do I get one order to find the ingredients on. 
    # I need to use a for loop to access each purchase. 
    menu_order_cost = 0 
    for purchase in purchases_objects:
        menu_item_object = purchase.menu_order 
        # recipe requirements is a list of data
        recipe_requirements = RecipeRequirement.objects.filter(recipe=menu_item_object)
        # we iterate over that list with a for loop and access the iteration variable quantity fields. 
        
        for requirement in recipe_requirements: 
            cost_per_ingredient = requirement.quantity * requirement.ingredient.price_per_unit
            menu_order_cost = menu_order_cost + cost_per_ingredient
    return menu_order_cost

    

    # the purchases are listed by names they do hold the ingredient data for each indvidual order. 

    

def home(request):
    return render(request,'inventory/home.html')

class MenuView(ListView):
    model = MenuItem
    template_name = 'inventory/menu.html'

class PurchaseView(ListView):
    model = Purchases
    template_name = 'inventory/purchases.html'

class IngredientsView(ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"