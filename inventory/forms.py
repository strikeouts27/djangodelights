from django import forms 
from .models import MenuItem, Ingredient, Purchases, RecipeRequirement

class MenuAdditionForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('__all__')

class IngredientAdditionForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('__all__')

class UpdateIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('__all__')

class RecipeAdditionForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('__all__')
class Purchases(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = ('__all__')
