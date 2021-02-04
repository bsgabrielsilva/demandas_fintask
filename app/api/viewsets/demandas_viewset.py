from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..serializers import DemandasCreateUpdateSerializer, DemandasListSerializer
from ...models import Demandas


class DemandasViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        serializer_class = DemandasListSerializer
        if self.request.method == 'PUT' or self.request.method == 'POST':
            serializer_class = DemandasCreateUpdateSerializer
        return serializer_class

    def get_queryset(self):
        cidade = self.request.query_params.get('cidade', None)
        if cidade is not None:
            return Demandas.objects.filter(user=self.request.user).\
                        filter(cidade__cidade__icontains=cidade).order_by('-updated_at')
        return Demandas.objects.filter(user=self.request.user).order_by('-updated_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
