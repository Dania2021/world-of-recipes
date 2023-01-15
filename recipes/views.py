from django.shortcuts import render
from django.views import generic, View
from .models import Recipe


class RecipeList(generic.ListView):
    model = Recipe
    recipe_list = Recipe.objects.all().order_by('-created_on')
    template_name = 'recipes_list.html'
    paginate_by = 6


class Home(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'index.html'
        )