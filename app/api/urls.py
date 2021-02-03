from rest_framework import routers

from django.urls import path, include
from .viewsets import *


router = routers.DefaultRouter()
router.register(r'cidades', CidadesViewSet, basename='cidades')

urlpatterns = [
    path('', include(router.urls)),
]
