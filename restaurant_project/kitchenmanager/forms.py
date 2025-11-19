from django import forms
from . import models
from django.forms.models import inlineformset_factory
from django.db.models import F
from django.db import transaction

# Ingredient model Forms
class IngredientCreationForm(forms.ModelForm):
    class Meta:
        model = models.Ingredient
        fields = ["name", "in_stock", "unit_type", "unit_price"]

        widgets = {
            "name" : forms.TextInput(attrs={"class": "form-control"}),
            "in_stock" : forms.NumberInput(attrs={"class": "form-control"}),
            "unit_type" : forms.TextInput(attrs={'class': 'form-control'}),
            "unit_price" : forms.NumberInput(attrs={"class": "form-control"}),
        }

# MenuItem model forms
class MenuItemCreationForm(forms.ModelForm):
    class Meta:
        model = models.MenuItem
        fields = ["name", "price","description"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }

# RecipeRequirement model forms
class RecipeRequirementCreationForm(forms.ModelForm):
    class Meta:
        model = models.RecipeRequirement
        fields = ["recipe", "ingredient", "quantity_needed"]

        widgets = {
            "ingredient": forms.Select(attrs={"class": "form-select"}),
            "quantity_needed": forms.NumberInput(attrs={"class": "form-control"}),
        }

RecipeRequirementFormSet = inlineformset_factory(
    models.MenuItem,
    models.RecipeRequirement,
    form=RecipeRequirementCreationForm,
    extra=3,
    can_delete=False
)

# Purchase model forms 
class PurchaseCreationForm(forms.ModelForm):
    class Meta:
        model = models.Purchase
        fields = ["menu_item"]
        
        widgets = {
            "menu_item": forms.Select(attrs={"class": "form-select"}),
        }

    def clean_menu_item(self):
        menu_item = self.cleaned_data["menu_item"]

        requirements = menu_item.requirements.all()
        stock_errors = []

        for req in requirements:
            if req.ingredient.in_stock < req.quantity_needed:
                stock_errors.append(f"Insufficient stock for '{req.ingredient.name}'. Need {req.quantity_needed} {req.ingredient.unit_type}, but only have {req.ingredient.in_stock} {req.ingredient.unit_type}.")
            
        if stock_errors:
            raise forms.ValidationError(stock_errors)
        
        return menu_item
            
            


