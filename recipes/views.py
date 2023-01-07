from django.shortcuts import render
from django.views import generic
from .models import Recipe


class RecipeList(generic.ListView):
    model = Recipe
    recipe_list = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
