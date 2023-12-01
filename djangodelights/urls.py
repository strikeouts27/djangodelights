# urls.py
from django.contrib import admin
from django.urls import path, include

# from inventory.views import finance, home, IngredientsView, MenuView, PurchaseView
from inventory import (
    views,
)  # with every view imported you need to specify views.viewname as seen in this file in the code below
from django.views.generic.base import TemplateView
from django.http import HttpResponse

urlpatterns = [
    path(
        "", views.home, name="default"
    ),  # users don't need to see the rocket page anyway. they need to see the home page.
    path("admin/", admin.site.urls),
    path("finance/", views.finance, name="finance"),
    path(
        "home/", views.home, name="home"
    ),  # I am attempting to connect the home_view function with the views function.
    path("ingredients/", views.IngredientsView.as_view(), name="ingredients"),
    path("menu/", views.MenuView.as_view(), name="menu"),
    path("purchases/", views.PurchaseView.as_view(), name="purchases"),
    path(
        "menu/add/",
        views.MenuAdditionView.as_view(success_url="/menu/"),
        name="menuadd",
    ),
    path(
        "ingredients/add/",
        views.IngredientAdditionView.as_view(success_url="/ingredients/"),
        name="ingredientadd",
    ),  # if class based view it requires an as_view
    path(
        "ingredient/update/<int:pk>",
        views.UpdateIngredientView.as_view(success_url="/ingredients/"),
        name="ingredientupdate",
    ),
    path(
        "recipe/add/",
        views.RecipeRequirementAdditionView.as_view(success_url="/menu/"),
        name="recipeadd",
    ),
    path(
        "purchases/add/",
        views.PurchaseAdditionView.as_view(success_url="/purchases/"),
        name="purchaseadd",
    ),
    path(
        "update/inventory/<int:pk>/",
        views.IngredientsListUpdateView.as_view(),
        name="updateinventory",
    ),
    path("item_details/<int:item_id>/", views.ItemDetails, name="item_details"),

    path("navbar/", views.navbar, name="navbar"),
]
# update view so the view had to be edited.}
# cannot have conflicting path names or matching names
# finance is not a classed based view therefore i do not need an as_view
# error message views.finance() type error means I a. calling the fucntion wrong or I am not supposed to be calling it.
# It needs to know what it is updating.
