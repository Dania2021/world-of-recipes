from .models import Recipe
from django import forms
from django.forms import ModelForm


class RecipeForm(forms.ModelForm):
    class Meta:
        # Associate the form with Recipe model and specify which fields to
        # display
        model = Recipe
        fields = ['title', 'ingredients', 'recipe_image',
                  'steps', 'serves', 'duration', 'skill_level',
                  'cuisine_name']

        labels = {
            'duration': 'Duration(in minutes)',
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'placeholder': 'Add Recipe name...'})
        self.fields['ingredients'].widget.attrs.update(
            {'placeholder': 'Use comma to separate items.'
             'Eg 50g oil, 50g flour, ..'})
        self.fields['steps'].widget.attrs.update(
            {'placeholder': 'Use a new line to add each step'})
        self.fields['serves'].widget.attrs.update(
            {'placeholder': 'e.g. 6...'})
        self.fields['duration'].widget.attrs.update(
            {'placeholder': 'e.g. 60...'})
