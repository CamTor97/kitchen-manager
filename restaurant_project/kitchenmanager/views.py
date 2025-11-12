from django.shortcuts import render
from django.views.generic import (ListView, DeleteView, DetailView, CreateView, UpdateView)
from django.urls import reverse_lazy
from .models import Ingredient, MenuItem, RecipeRequirements, Purchase
# Create your views here.
# Ingredient model views
class IngredientListView(ListView):
    model = Ingredient
    template_name = ""
    context_object_name = "ingredient" 

class IngredientCreationView(CreateView):
    model = Ingredient
    fields = ["name", "in_stock", "unit_type", "unit_price"]
    template_name = ""
    success_url= reverse_lazy("")

class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = ["name", "in_stock", "unit_type", "unit_price"]
    template_name = ""
    success_url= reverse_lazy("")

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = ""
    success_url = reverse_lazy("")

