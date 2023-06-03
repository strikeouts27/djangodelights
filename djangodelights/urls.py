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
from inventory.views import finance, home, IngredientsView, MenuView, PurchaseView
from inventory import views
from django.views.generic.base import TemplateView
from django.http import HttpResponse

urlpatterns = [
    
    path('', views.home, name='default'), # users don't need to see the rocket page anyway. they need to see the home page.
    path('admin/', admin.site.urls),
    path('finance/', finance, name='finance'),
    path('home/', home, name='home'), #I am attempting to connect the home_view function with the views function.
    path('ingredients/', IngredientsView.as_view(), name='ingredients'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('purchases/', PurchaseView.as_view(), name='purchases'),
    ]
