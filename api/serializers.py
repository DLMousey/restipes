from rest_framework import serializers
from . import models


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = ('name', 'amount', 'measurement')


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = models.Recipe
        fields = ('id', 'slug', 'name', 'description', 'cooking_instructions', 'cooking_time', 'preparation_time',
                  'ingredients', 'created', 'modified')


class RecipeSummarySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return '/api/recipes/{}'.format(obj.slug)

    class Meta:
        model = models.Recipe
        url = serializers.CharField(source='get_url')
        fields = ('id', 'name', 'description', 'url')
