from django.contrib import admin
from .models import Recipe, Comment, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'skill_level', 'created_on')
    search_fields = ['cuisine_name', 'author']
    list_filter = ('skill_level', 'created_on')
    summernote_fields = 'steps'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('author', 'body', 'created_on', 'recipe', 'approved')
    search_fields = ['author', 'recipe']
    list_filter = ('author',)
    actions = ['comments_disapproved']

    def comments_disapproved(self, request, queryset):
        queryset.update(approved=False)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'profile_first_name', 'profile_last_name')
    search_fields = ['user', 'profile_first_name']
    list_filter = ('user',)
