from . import views
from django.urls import path


urlpatterns = [
    path(
        'recipes_list/',
        views.RecipeList.as_view(), name='recipes_list'),
]
