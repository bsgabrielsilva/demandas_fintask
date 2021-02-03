from rest_framework import serializers
from .cidades_serializer import CidadesSerializer
from ...models import Demandas


"""
    Usar essa abordagem abaixo, não é uma das melhores, eu sei. Mas economiza o tempo necessário para 
    a entrega do projeto.
"""


class BaseDemandasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demandas
        fields = ('id', 'descricao', 'status', 'logradouro', 'complemento', 'bairro', 'cep', 'cidade',
                  'email', 'telefone', 'celular')


class DemandaStatusUpdateSerializer(BaseDemandasSerializer):
    def __init__(self, *args, **kwargs):
        super(DemandaStatusUpdateSerializer, self).__init__(*args, **kwargs)
        self.fields.pop('descricao')
        self.fields.pop('logradouro')
        self.fields.pop('complemento')
        self.fields.pop('bairro')
        self.fields.pop('cep')
        self.fields.pop('cidade')
        self.fields.pop('email')
        self.fields.pop('telefone')
        self.fields.pop('celular')


class DemandasCreateUpdateSerializer(BaseDemandasSerializer):
    def __init__(self, *args, **kwargs):
        super(DemandasCreateUpdateSerializer, self).__init__(*args, **kwargs)
        self.fields.get('status').read_only = True


class DemandasListSerializer(BaseDemandasSerializer):
    def __init__(self, *args, **kwargs):
        super(DemandasListSerializer, self).__init__(*args, **kwargs)

    cidade = CidadesSerializer(many=False, read_only=False)


