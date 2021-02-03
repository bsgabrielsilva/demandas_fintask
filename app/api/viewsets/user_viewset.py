from django.contrib.auth.models import User
from rest_framework import viewsets
from ..serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(user=self.request.user)