from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect


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


class Profile(View):
    
    def get(self, request, *args, **kwargs):
        my_recipes = Recipe.objects.filter(author=request.user)
        return render(
            request,
            'recipe.html',
            {
                'my_recipes': my_recipes,
            },
        )


class RecipeDetail(View):
    model = Recipe
    fields = '__all__'

    def get(self, request, id, *args, **kwargs):
        recipe_detail = Recipe.objects.all()
        recipe = get_object_or_404(recipe_detail, id=id)
        comments = recipe.comments.filter(approved=True)
        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments
            },
        )


class AddRecipeView(View):

    def get(self, request):
        add_form = RecipeForm()

        return render(
            request,
            'recipe_add.html',
            {
                'add_form': add_form,
            },
        )

    def post(self, request):
        add_form = RecipeForm(request.POST, request.FILES)
        if add_form.is_valid():
            add_form.instance.author = request.user
            add_form.save()
            messages.success(request, 'Recipe Added Successfully')
        else:
            recipe_form = RecipeForm()
            messages.error(
                request, 'There was an error submitting your recipe.')

        return HttpResponseRedirect(reverse('home'))


class UpdateRecipeView(View):

    def get(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        update_form = RecipeForm(instance=recipe)

        return render(
            request,
            'recipe_edit.html',
            {
                'update_form': update_form,
                'recipe': recipe,
            }
        )

    def post(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        update_form = RecipeForm(
            request.POST, request.FILES, instance=recipe)

        if update_form.is_valid():
            update_form.clean()
            update_form.save()
            messages.success(request, 'Recipe Updated') 
        else:
            update_form = RecipeForm(instance=recipe)
            messages.error(request, 'Your Recipe has not been Updated')
     
        return HttpResponseRedirect(reverse('recipe'))


class Recipes(View):

    def get(self, request, id, *args, **kwargs):
        recipe = get_object_or_404(Recipe, id=id)
        return render(
            request,
            'recipes.html',
            {
                'recipe': recipe,
            }
        )