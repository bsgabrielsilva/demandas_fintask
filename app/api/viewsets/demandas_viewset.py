from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..serializers import DemandasSerializer
from ...models import Demandas


class DemandasViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = DemandasSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        cidade = self.request.query_params.get('cidade', None)
        if cidade is not None:
            return Demandas.objects.filter(user=self.request.user).\
                        filter(cidade__icontains=cidade).order_by('-updated_at')
        return Demandas.objects.filter(user=self.request.user).order_by('-updated_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
