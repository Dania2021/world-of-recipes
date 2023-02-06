from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Recipe, Comment


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''
    To create a user profile when new user is registered
    '''
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    '''
    To save a user profile when new user is created
    '''
    instance.profile.save()


@receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    '''
    To delete recipe and comments when profile is deleted
    '''
    Recipe.objects.filter(author=instance.user).delete()
    Comment.objects.filter(author=instance.user).delete()
