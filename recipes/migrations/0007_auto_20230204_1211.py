# Generated by Django 3.2.16 on 2023-02-04 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20230131_0112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_created',
        ),
    ]