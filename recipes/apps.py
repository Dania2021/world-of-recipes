from django.apps import AppConfig


class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'

    # to connect the receiver in ready method
    def ready(self):
        import recipes.signals
