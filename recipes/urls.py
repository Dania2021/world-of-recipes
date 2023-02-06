from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path(
        'recipes_list/',
        views.RecipeList.as_view(), name='recipes_list'),
    path(
        'recipe_detail/<int:id>/',
        views.RecipeDetail.as_view(), name='recipe_detail'),
    path(
        'recipe_add/', views.AddRecipeView.as_view(), name='recipe_add'),
    path(
        'recipe/',
        views.ProfileView.as_view(), name='recipe'),
    path(
        'recipe_edit/<int:id>/',
        views.UpdateRecipeView.as_view(), name='recipe_edit'),
    path(
        'recipes/<int:id>/',
        views.Recipes.as_view(), name='recipes'),
    path(
        'recipe_delete/<int:id>/',
        views.DeleteRecipeView.as_view(), name='recipe_delete'),
    path('profile/', views.ProfileAddView.as_view(), name='profile'),
    path(
        'edit_profile/',
        views.ProfileEditView.as_view(), name='edit_profile'),
    path(
        'profile_delete/',
        views.ProfileDeleteView.as_view(), name='profile_delete'),
        ]
