from django.shortcuts import render
from rest_framework import viewsets

from . import serializers
from . import models


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = models.Recipe.objects.all()
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RecipeSummarySerializer

        return serializers.RecipeSerializer
