from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..serializers import CidadesSerializer
from ...models import Cidades


class CidadesViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = CidadesSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        cidade = self.request.query_params.get('cidade', None)
        if cidade is not None:
            return Cidades.objects.filter(cidade__icontains=cidade).order_by('-updated_at')
        return Cidades.objects.all().order_by('-updated_at')
