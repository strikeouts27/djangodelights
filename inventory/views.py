from django.shortcuts import render
from django.urls import path 
from .models import Ingredient, MenuItem, Purchases
from django.views.generic import ListView

from django.http import HttpResponse

# Create your views here.

def finance(request):
    purchased_items = Purchases.objects.all() # this grabs every row in the purchases table

    total_revenue = 0 
    for item in purchased_items:
        total_revenue = total_revenue + item.menu_order.price #this uses the price of each item to calculate the revenue
    
    # i want the price of the item and the cost of each item.
    total_cost = 0
    
    
# str method made it django djaffa cake
        # this grabs the menu item with all of its data.
        # and then we want to get the price of that menu item.
        # price was accessed by dot notation to get the price for that single item that was purchased.
     


    return render(request,'inventory/finance.html')

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