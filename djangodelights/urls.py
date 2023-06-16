"""
URL configuration for djangodelights project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from inventory.views import finance, home, IngredientsView, MenuView, PurchaseView
from inventory import views # with every view imported you need to specify views.viewname as seen in this file in the code below
from django.views.generic.base import TemplateView
from django.http import HttpResponse

urlpatterns = [
    
    path('', views.home, name='default'), # users don't need to see the rocket page anyway. they need to see the home page.
    path('admin/', admin.site.urls),
    path('finance/', views.finance, name='finance'),
    path('home/', views.home, name='home'), #I am attempting to connect the home_view function with the views function.
    path('ingredients/', views.IngredientsView.as_view(), name='ingredients'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('purchases/', views.PurchaseView.as_view(), name='purchases'), 
    path('menu/add',views.MenuAdditionView.as_view(success_url = "/menu/"), name="menuadd"),
    path('ingredients/add', views.IngredientAdditionView.as_view(success_url = "/ingredients/"), name='ingredientadd'), # if class based view it requires an as_view
    # path('ingredient/update', views.UpdateIngredientView.as_view(), name='ingredientupdate'),
    path('recipe/add', views.RecipeRequirementAdditionView.as_view(success_url = "/menu/"), name='recipeadd'),
    path('purchases/add', views.PurchaseAdditionView.as_view(success_url = "/purchases/"), name = 'purchaseaddition'),
    # path('finance/', views.finance(), name='finance'), # this line of code holds the error.
    # finance is not a classed based view therefore i do not need an as_view
    # error message views.finance() type error means I a. calling the fucntion wrong or I am not supposed to be calling it.
    ]
