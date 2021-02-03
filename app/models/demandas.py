from django.db import models
from ..utils import demandas_choices
from ..abstracts import TimestampsAbstract


class Demandas(TimestampsAbstract, models.Model):
    descricao = models.TextField('Descrição da peça', null=False)
    status = models.CharField('Status de Finalização', max_length=20, choices=demandas_choices())

    logradouro = models.CharField('Endereço/Logradouro com número', max_length=254, null=False)
    complemento = models.CharField('Complemento', max_length=254, null=False)
    bairro = models.CharField('Bairro', max_length=254, null=False)
    cep = models.CharField('Cep', max_length=9, null=False)

    email = models.EmailField('Email para contato', max_length=254, null=False)
    telefone = models.CharField('Telefone', max_length=14, null=False)
    celular = models.CharField('Celular', max_length=14, null=False)

    cidade = models.ForeignKey('app.Cidades', on_delete=models.PROTECT, related_name='demandas')
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='demandas')

    class Meta:
        app_label = 'app'
        verbose_name = 'Demandas'
        verbose_name_plural = 'Demandas de Peças'
