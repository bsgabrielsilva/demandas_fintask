from rest_framework import routers

from django.urls import path, include
from .viewsets import *


router = routers.DefaultRouter()
router.register(r'cidades', CidadesViewSet, basename='cidades')
router.register(r'demandas', DemandasViewSet, basename='demandas')

urlpatterns = [
    path('', include(router.urls)),
]
