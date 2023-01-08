from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


SKILL_LEVEL = ((0, 'Beginners'), (1, 'Intermediate'), (2, 'Advanced'))


class Recipe(models.Model):
    '''
    To create recipe where user can add a recipe
    '''
    AMERICAN = 'American'
    BRITISH = 'British'
    CHINESE = 'Chinese'
    EUROPEAN = 'European'
    FRENCH = 'French'
    GERMAN = 'German'
    GREEK = 'Greek'
    INDIAN = 'Indian'
    INDONESIAN = 'Indonesian'
    IRISH = 'Irish'
    ITALIAN = 'Italian'
    JAPANESE = 'Japanese'
    KOREAN = 'Korean'
    MEXICAN = 'Mexican'
    SPANISH = 'Spanish'
    THAI = 'Thai'
    TURKISH = 'Turkish'

    CUISINE_CHOICES = [
        (AMERICAN, 'American'),
        (BRITISH, 'British'),
        (CHINESE, 'Chinese'),
        (EUROPEAN, 'European'),
        (FRENCH, 'French'),
        (GERMAN, 'German'),
        (GREEK, 'Greek'),
        (INDIAN, 'Indian'),
        (INDONESIAN, 'Indonesian'),
        (IRISH, 'Irish'),
        (ITALIAN, 'Italian'),
        (JAPANESE, 'Japanese'),
        (KOREAN, 'Korean'),
        (MEXICAN, 'Mexican'),
        (SPANISH, 'Spanish'),
        (THAI, 'Thai'),
        (TURKISH, 'Turkish')
    ]

    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_posts')
    ingredients = models.TextField()
    recipe_image = CloudinaryField('image', default='placeholder')
    steps = models.TextField()
    serves = models.IntegerField()
    duration = models.IntegerField()
    skill_level = models.IntegerField(choices=SKILL_LEVEL, default=0)
    cuisine_name = models.CharField(
        max_length=30, choices=CUISINE_CHOICES, default=AMERICAN)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        order recipe by newest first
        '''
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    '''
    To leave comments on recipes
    '''
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        '''
        order comment by oldest first
        '''
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.author} on Recipe {self.recipe}'
