from django.shortcuts import render, get_object_or_404
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


class RecipeDetail(View):
    model = Recipe
    fields = '__all__'

    def get(self, request, author_id, *args, **kwargs):
        recipe_detail = Recipe.objects.all()
        recipe = get_object_or_404(recipe_detail, id=author_id)
        comments = recipe.comments.filter(approved=True)
        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments
            },
        )
