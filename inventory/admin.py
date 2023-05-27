from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement, Purchases # models is looking for a generic python package. when you say .models it says look for models in my directory.

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)
admin.site.register(Purchases)
