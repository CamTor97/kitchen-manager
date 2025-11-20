from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.views.generic import (ListView, DeleteView, DetailView, CreateView, UpdateView, TemplateView, View)
from django.urls import reverse_lazy
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .mixins import CalculatedVariablesMixin
from .forms import IngredientCreationForm, MenuItemCreationForm, RecipeRequirementFormSet, PurchaseCreationForm
# Create your views here.
def logout_view(request):
    logout(request)
    return redirect("login")

# Dashboard view
class DashboardView(CalculatedVariablesMixin, TemplateView):
    template_name = "kitchenmanager/dashboard.html"

    
# Ingredient model views
class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "kitchenmanager/ingredients.html"
    context_object_name = "ingredient" 

class IngredientCreationView(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientCreationForm
    template_name = "kitchenmanager/ingredient-create.html"
    success_url= reverse_lazy("ingredients")

class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientCreationForm
    template_name = "kitchenmanager/ingredient-create.html"
    success_url= reverse_lazy("ingredients")

class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "kitchenmanager/ingredient_confirm_delete.html"
    success_url = reverse_lazy("ingredients")

#MenuItem model views
class MenuItemListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "kitchenmanager/menu.html"
    context_object_name = "menu_item"

class MenuItemCreationView(LoginRequiredMixin, View):
    template_name = "kitchenmanager/menu_item-create.html"
    success_url = reverse_lazy("menu_items")
    
    def get(self, request):
        context = {
            "form": MenuItemCreationForm(),
            "formset": RecipeRequirementFormSet(queryset=RecipeRequirement.objects.none())
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        menuitem_form = MenuItemCreationForm(request.POST)
        formset = RecipeRequirementFormSet(request.POST)
        if menuitem_form.is_valid() and formset.is_valid():
            with transaction.atomic():
                menuitem_instance = menuitem_form.save()
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.recipe = menuitem_instance
                    instance.save()
            return redirect(self.success_url)
        
        context = {"form": menuitem_form, "formset": formset}
        return render(request, self.template_name, context)

    

class MenuItemUpdateView(LoginRequiredMixin, View):
    template_name = "kitchenmanager/menu_item-create.html"
    success_url = reverse_lazy("menu_items")
    
    def get(self, request, pk):
        menu_item_instance = get_object_or_404(MenuItem, pk=pk)
        context = {
            "form": MenuItemCreationForm(instance=menu_item_instance),
            "formset": RecipeRequirementFormSet(instance=menu_item_instance) 
        }
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        recipe_instance = get_object_or_404(MenuItem, pk=pk)
        menuitem_form = MenuItemCreationForm(request.POST, instance=recipe_instance)
        formset = RecipeRequirementFormSet(request.POST, instance=recipe_instance)
        if menuitem_form.is_valid() and formset.is_valid():
            with transaction.atomic():
                menuitem_instance = menuitem_form.save()
                instances = formset.save(commit=False)
                for instance in instances:
                    instance.recipe = menuitem_instance
                    instance.save()
            return redirect(self.success_url)
        
        context = {"form": menuitem_form, "formset": formset}
        return render(request, self.template_name, context)

class MenuItemDeleteView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = "kitchenmanager/menu_item_confirm_delete.html"
    success_url = reverse_lazy("menu_items")

class MenuItemDetailView(LoginRequiredMixin, DetailView):
    model = MenuItem
    template_name = "kitchenmanager/menu-details.html"
    context_object_name = "menu_item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding the recipe requirements for this item
        context["requirements"] = RecipeRequirement.objects.filter(recipe=self.object)
        return context 

# RecipeRequirement model views
class RecipeRequirementListView(LoginRequiredMixin, ListView):
    model = RecipeRequirement
    template_name = ""
    context_object_name = "recipe_requirement"

class RecipeRequirementCreationView(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    fields = ["recipe", "ingredient", "quantity_need"]
    template_name = ""
    success_url = reverse_lazy("recipe_requirements")

class RecipeRequirementUpdateView(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    fields = ["recipe", "ingredient", "quantity_need"]
    template_name = ""
    success_url = reverse_lazy("recipe_requirements")

class RecipeRequirementDeleteView(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = ""
    success_url = reverse_lazy("recipe_requirements")

# Purchase model views
class PurchaseListView(LoginRequiredMixin, CalculatedVariablesMixin, ListView):
    model = Purchase
    template_name = "kitchenmanager/purchases.html"
    context_object_name = "purchase"

class PurchaseCreationView(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = PurchaseCreationForm
    template_name = "kitchenmanager/purchase-create.html"
    success_url = reverse_lazy("purchases")

class PurchaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Purchase
    fields = ["menu_item"]
    template_name = ""
    success_url = reverse_lazy("purchases")

class PurchaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = "kitchenmanager/purchase_confirm_delete.html"
    success_url = reverse_lazy("purchases")
    

