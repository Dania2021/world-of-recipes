from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'status', 'created_on')
    search_fields = ['cuisine_name', 'author']
    list_filter = ('status', 'created_on')
    summernote_fields = 'steps'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('author', 'body', 'created_on', 'recipe', 'approved')
    search_fields = ['author', 'recipe']
    list_filter = ('author',)
    actions = ['comments_approved']

    def comments_approved(self, request, queryset):
        queryset.update(approved=True)