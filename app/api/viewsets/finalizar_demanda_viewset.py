from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..serializers import DemandaStatusUpdateSerializer
from ...models import Demandas


class FinalizarDemandaViewSet(viewsets.ModelViewSet):
    http_method_names = ['put']
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    serializer_class = DemandaStatusUpdateSerializer

    def get_queryset(self):
        return Demandas.objects.filter(user=self.request.user).order_by('-updated_at')

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data['status'] == "Finalizada" and instance.status != "Finalizada":
            instance = serializer.save()
            self.perform_update(instance)
            headers = self.get_success_headers(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT, headers=headers)
        elif instance.status == "Finalizada":
            return Response({'message': 'Demanda já finalizada!'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Você só pode finalizar esta demanda.'}, status=status.HTTP_401_UNAUTHORIZED)
