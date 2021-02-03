from django.db import models
from ..abstracts import TimestampsAbstract
from ..utils import estados_choices


class Cidades(TimestampsAbstract, models.Model):

    slug = models.SlugField('Slug', max_length=254, null=False, primary_key=True, unique=True)
    cidade = models.CharField('Cidade', max_length=254, null=False)
    estado = models.CharField('Estado', max_length=50, null=False, choices=estados_choices(), default='Amapá')

    def __str__(self):
        return f'{self.cidade} - {self.estado}'

    class Meta:
        app_label = 'app'
        verbose_name = 'Cidades'
        verbose_name_plural = 'Cidades'

