from rest_framework import serializers
from .cidades_serializer import CidadesSerializer
from ...models import Demandas


class DemandasSerializer(serializers.ModelSerializer):
    cidade = CidadesSerializer(many=False, read_only=False)

    class Meta:
        model = Demandas
        fields = ('id', 'descricao', 'status', 'logradouro', 'complemento', 'bairro', 'cep', 'cidade',
                  'email', 'telefone', 'celular')
