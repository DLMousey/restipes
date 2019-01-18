from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    cooking_instructions = models.TextField()
    slug = models.SlugField()
    preparation_time = models.IntegerField(help_text='Preperation time in minutes')
    cooking_time = models.IntegerField(help_text='Cooking time in minutes')
    created = models.DateTimeField()
    modified = models.DateTimeField()


class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    amount = models.IntegerField()
    measurement = models.CharField(max_length=150)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='ingredients')
