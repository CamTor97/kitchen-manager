from django.shortcuts import render
from django.views.generic import (ListView, DeleteView, DetailView, CreateView, UpdateView, TemplateView)
from django.urls import reverse_lazy
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .mixins import CalculatedVariablesMixin
# Create your views here.
# Dashboard view
class DashboardView(CalculatedVariablesMixin, TemplateView):
    template_name = "kitchenmanager/dashboard.html"

    
# Ingredient model views
class IngredientListView(ListView):
    model = Ingredient
    template_name = "kitchenmanager/ingredients.html"
    context_object_name = "ingredient" 

class IngredientCreationView(CreateView):
    model = Ingredient
    fields = ["name", "in_stock", "unit_type", "unit_price"]
    template_name = ""
    success_url= reverse_lazy("ingredients")

class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = ["name", "in_stock", "unit_type", "unit_price"]
    template_name = ""
    success_url= reverse_lazy("ingredients")

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = ""
    success_url = reverse_lazy("ingredients")

#MenuItem model views
class MenuItemListView(ListView):
    model = MenuItem
    template_name = "kitchenmanager/menu.html"
    context_object_name = "menu_item"

class MenuItemCreationView(CreateView):
    model = MenuItem
    fields = ["name", "price", "description"]
    template_name = ""
    success_url = reverse_lazy("menu_items")

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    fields = ["name", "price", "description"]
    template_name = ""
    success_url = reverse_lazy("menu_items")

class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = ""
    success_url = reverse_lazy("menu_items")

class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = "kitchenmanager/menu-details.html"
    context_object_name = "menu_item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding the recipe requirements for this item
        context["requirements"] = RecipeRequirement.objects.filter(recipe=self.object)
        return context 

# RecipeRequirement model views
class RecipeRequirementListView(ListView):
    model = RecipeRequirement
    template_name = ""
    context_object_name = "recipe_requirement"

class RecipeRequirementCreationView(CreateView):
    model = RecipeRequirement
    fields = ["recipe", "ingredient", "quantity_need"]
    template_name = ""
    success_url = reverse_lazy("recipe_requirements")

class RecipeRequirementUpdateView(UpdateView):
    model = RecipeRequirement
    fields = ["recipe", "ingredient", "quantity_need"]
    template_name = ""
    success_url = reverse_lazy("recipe_requirements")

class RecipeRequirementDeleteView(DeleteView):
    model = RecipeRequirement
    template_name = ""
    success_url = reverse_lazy("recipe_requirements")

# Purchase model views
class PurchaseListView(CalculatedVariablesMixin, ListView):
    model = Purchase
    template_name = "kitchenmanager/purchases.html"
    context_object_name = "purchase"

class PurchaseCreationView(CreateView):
    model = Purchase
    fields = ["menu_item"]
    template_name = ""
    success_url = reverse_lazy("purchases")

class PurchaseUpdateView(UpdateView):
    model = Purchase
    fields = ["menu_item"]
    template_name = ""
    success_url = reverse_lazy("purchases")

class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = ""
    success_url = reverse_lazy("purchases")
    

