from django.shortcuts import render
from django.views.generic import (ListView, DeleteView, DetailView, CreateView, UpdateView, TemplateView)
from django.urls import reverse_lazy
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.db.models import Sum, F
# Create your views here.
# Dashboard view
class DashboardView(TemplateView):
    template_name = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculating Total Revenue
        total_revenue = Purchase.objects.aaggregate(
            total=Sum("menu_item__price")
        )["total"] or 0
        # Calculating Total Costs
        total_cost = Purchase.objects.aaggregate(
            total=Sum(
                F("menu_item__reciperequirement__quantity_needed") *
                F("menu_item__reciperequirement__ingredient__unit_price")
            )
        )["total"] or 0
        # Calculating Total Profit
        total_profit = total_revenue - total_cost
        # Updating context
        context.update({
            "total_revenue": total_revenue,
            "total_cost": total_cost,
            "total_profit": total_profit,
        })
        return context
    
# Ingredient model views
class IngredientListView(ListView):
    model = Ingredient
    template_name = ""
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
    template_name = ""
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
    template_name = ""
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
class PurchaseListView(ListView):
    model = Purchase
    template_name = ""
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
    

