"""
URL configuration for restaurant_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from kitchenmanager import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", auth_views.LoginView.as_view(template_name="kitchenmanager/login.html"), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    # Ingredient model Urls
    path("ingredients/", views.IngredientListView.as_view(), name="ingredients"),
    path("ingredients/create/", views.IngredientCreationView.as_view(), name="ingredient-create"),
    path("ingredients/<int:pk>/update", views.IngredientUpdateView.as_view(), name="ingredient-update"),
    path("ingredients/<int:pk>/delete", views.IngredientDeleteView.as_view(), name="ingredient-delete"),
    # MenuItem model Urls
    path("menu_items/", views.MenuItemListView.as_view(), name="menu_items"),
    path("menu_items/create/", views.MenuItemCreationView.as_view(), name="menu_items-create"),
    path("menu_items/<int:pk>/", views.MenuItemDetailView.as_view(), name="menu_items-detail"),
    path("menu_items/<int:pk>/update", views.MenuItemUpdateView.as_view(), name="menu_items-update"),
    path("menu_items/<int:pk>/delete", views.MenuItemDeleteView.as_view(), name="menu_items-delete"),
    # RecipeRequirement model Urls
    path("recipe_requirements/", views.RecipeRequirementListView.as_view(), name="recipe_requirements"),
    path("recipe_requirements/create/", views.RecipeRequirementCreationView.as_view(), name="recipe_requirements-create"),
    path("recipe_requirements/<int:pk>/update", views.RecipeRequirementUpdateView.as_view(), name="recipe_requirements-update"),
    path("recipe_requirements/<int:pk>/delete", views.RecipeRequirementDeleteView.as_view(), name="recipe-requirements-delete"),
    # Purchase model Urls"
    path("purchases/", views.PurchaseListView.as_view(), name="purchases"),
    path("purchases/create", views.PurchaseCreationView.as_view(), name="purchases-create"),
    path("purchases/<int:pk>/update", views.PurchaseUpdateView.as_view(), name="purchases-update"),
    path("purchases/<int:pk>/delete", views.PurchaseDeleteView.as_view(), name="purchases-delete"),

    
]
