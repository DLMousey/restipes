from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('recipes', views.RecipeViewSet)


urlpatterns = [
    path('', include(router.urls))
]