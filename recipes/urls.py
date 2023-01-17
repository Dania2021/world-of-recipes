from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path(
        'recipes_list/',
        views.RecipeList.as_view(), name='recipes_list'),
    path(
        'recipe_detail/<int:author_id>/',
        views.RecipeDetail.as_view(), name='recipe_detail'),    
]
