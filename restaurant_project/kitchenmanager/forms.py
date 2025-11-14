from django import forms
from . import models
from django.forms.models import inlineformset_factory

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

