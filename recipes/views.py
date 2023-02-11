from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Recipe, Comment, Profile
from .forms import RecipeForm, CommentForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.db.models import Q


class RecipeList(generic.ListView):
    '''
    To display the list of recipes
    '''
    model = Recipe
    recipe_list = Recipe.objects.all().order_by('-created_on')
    template_name = 'recipes_list.html'
    paginate_by = 6


class Home(View):
    '''
    The site homepage
    '''
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'index.html'
        )


class ProfileView(View):
    '''
    To display the user profile with update and
    delete buttons and display user's recipes
    '''
    def get(self, request):
        profile_queryset = Profile.objects.filter(user=request.user)
        profile = get_object_or_404(profile_queryset)
        my_recipes = Recipe.objects.filter(author=request.user)

        return render(
            request,
            'recipe.html',
            {
                'my_recipes': my_recipes,
                'profile': profile,
            },
        )


class RecipeDetail(View):
    '''
    To display the detail view of recipe and
    comment form for authenticated users
    '''
    model = Recipe
    fields = '__all__'

    def get(self, request, id, *args, **kwargs):
        recipe_detail = Recipe.objects.all()
        recipe = get_object_or_404(recipe_detail, id=id)
        comments = recipe.comments.filter(approved=True)
        comment_form = CommentForm()
        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'comment_form': comment_form,
            },
        )

    def post(self, request, id, *args, **kwargs):
        recipe_detail = Recipe.objects.all()
        recipe = get_object_or_404(recipe_detail, id=id)
        comments = recipe.comments.filter(approved=True)

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.success(request, 'Comment Added')
            return redirect('recipe_detail', id=id)
        else:
            comment_form = CommentForm()
            messages.error(
                request, 'There was an error submitting your comment.')

        return render(
            request,
            'recipe_detail.html',
            {
                'recipe': recipe,
                'comments': comments,
                'comment_form': comment_form,
            },
        )


class AddRecipeView(View):
    '''
    To display form to upload recipe by authenticated user
    '''
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
    '''
    To display form to update recipe
    '''
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
    '''
    To display the detail view of recipe with
    update and delete buttons
    '''
    def get(self, request, id, *args, **kwargs):
        recipe = get_object_or_404(Recipe, id=id)
        return render(
            request,
            'recipes.html',
            {
                'recipe': recipe,
            }
        )


class DeleteRecipeView(View):
    '''
    To display a modal to delete a recipe
    '''
    def post(self, request, id, *args, **kwargs):
        recipe = get_object_or_404(Recipe, id=id)

        recipe.delete()
        messages.success(request, 'Your recipe has been deleted')

        return HttpResponseRedirect(reverse('recipe'))


class ProfileAddView(View):
    '''
    To display a form to add user's profile
    '''
    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        profile_form = ProfileForm(instance=profile)

        return render(
            request,
            'profile.html',
            {
                'profile_form': profile_form,
            },
        )

    def post(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile)

        if profile_form.is_valid():
            profile_form.instance.user = request.user
            profile_form.save()
            messages.success(request, 'Profile Added Successfully')
        else:
            profile_form = ProfileForm()
            messages.error(
                request, 'There was an error submitting your profile.')

        return HttpResponseRedirect(reverse('recipe'))


class ProfileEditView(View):
    '''
    To display a form for user to update profile
    '''
    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)
        update_profile = ProfileForm(instance=profile)

        return render(
            request,
            'edit_profile.html',
            {
                'profile': profile,
                'update_profile': update_profile,
            }
        )

    def post(self, request):
        profile_queryset = Profile.objects.filter(user=request.user)
        get_object_or_404(profile_queryset)
        profile = profile_queryset.first()
        update_profile = ProfileForm(
            request.POST, request.FILES, instance=profile)

        if update_profile.is_valid():
            update_profile.clean()
            update_profile.save()
            messages.success(request, 'Profile Updated successfully')
        else:
            update_profile = ProfileEditForm(instance=request.user.profile)
            messages.error(request, 'Your profile has not updated')

        return HttpResponseRedirect(reverse('recipe'))


class ProfileDeleteView(View):
    '''
    To display a modal to delete user's profile
    '''
    def post(self, request):
        user = request.user
        user.delete()
        messages.success(request, 'Your Profile Deleted successfully')
        logout(request)
        return HttpResponseRedirect(reverse('home'))


class RecipeSearchView(View):
    '''To display the search page'''
    paginate_by = 6

    def post(self, request, *args, **kwargs):
        searched = request.POST['searched']
        recipes = Recipe.objects.filter(
            Q(ingredients__icontains=searched) |
            Q(title__icontains=searched),
            )
        return render(
            request,
            'search_results.html',
            {
                'searched': searched,
                'recipes': recipes,
            }
            )
