from rest_framework import routers

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .viewsets import *


router = routers.DefaultRouter()
router.register(r'cidades', CidadesViewSet, basename='cidades')
router.register(r'demandas', DemandasViewSet, basename='demandas')
router.register(r'registro', UserViewSet, basename='registro')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token)
]
