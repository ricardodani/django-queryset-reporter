'''
Models of queryset_reporter.
'''

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

from queryset_reporter import mapping
from queryset_reporter import settings

_NULL = {'null': True, 'blank': True}
_CHAR = {'max_length': 255, 'blank': False}
_CNULL = _CHAR
_CNULL.update(_NULL)


class Queryset(models.Model):
    '''Queryset is a model representation of a generic Model.
    '''

    # metadata
    name = models.CharField(_(u'Nome'), **_CHAR)
    desc = models.TextField(_(u'Descrição'), **_CHAR)
    model = models.ForeignKey(
        ContentType, verbose_name=_(u'Modelo'),
        on_delete=models.CASCADE
    )
    distinct = models.BooleanField(_(u'Distinguir'), default=False)

    # timestamps
    created_at = models.DateTimeField(_(u'Criação'), auto_now_add=True)
    modified_at = models.DateTimeField(_(u'Modificação'), auto_now=True)

    # automatic generation
    automatic_generation = models.BooleanField(
        _(u'Geração Automática'), default=False)
    last_automatic_generation_at = models.DateTimeField(
        _(u'Última geração automática'), editable=False, **_NULL)
    last_automatic_generation_xlsx = models.CharField(
        _(u'Último relatório gerado em XLSX'), max_length=250,
        editable=False, **_NULL)

    def __str__(self):
        return f'[{self.model.name}] {self.name}'

    class Meta:
        verbose_name = _(u'Modelo de Queryset')
        verbose_name_plural = _(u'Modelos de Queryset')
        permissions = (
            ('can_use_reports', 'Prever e gerar relatórios'),
        )

    def get_absolute_url(self):
        path = reverse('queryset_reporter:qr_create')
        return f'{path}?queryset={self.id}'


class FieldModel(models.Model):
    queryset = models.ForeignKey(Queryset, on_delete=models.CASCADE)
    field = models.CharField(_(u'Código do Campo'), **_CHAR)
    field_verbose = models.CharField(_(u'Nome do Campo'), **_CHAR)
    field_type = models.CharField(_(u'Tipo do Campo'), **_CHAR)

    class Meta:
        abstract = True


class DisplayField(FieldModel):
    '''Or the Fields and Extras selects called in .values().
    '''

    sort = models.CharField(
        verbose_name=_(u'Ordenação'), max_length=4, choices=(
            ('asc', _(u'Crescente')),
            ('desc', _(u'Decrescente'))
        ), default=None, **_NULL
    )
    annotate = models.CharField(
        verbose_name=_(u'Anotação'), max_length=5, choices=(
            ('Count', _(u'Somatório')),
            ('Ave', _(u'Média')),
            ('Max', _(u'Máximo')),
            ('Min', _(u'Mínimo')),
        ), **_NULL
    )
    position = models.PositiveSmallIntegerField(**_NULL)

    pre_concatenate = models.CharField(
        verbose_name=_(u'Pré concatenação'), **_CNULL
    )
    pos_concatenate = models.CharField(
        verbose_name=_(u'Pós concatenação'), **_CNULL
    )

    def __str__(self):
        return self.field_verbose

    @property
    def get_field(self):
        if not self.annotate:
            return self.field
        else:
            return '%s_%s' % (self.annotate, self.field.replace('__', '_'))

    class Meta:
        verbose_name = _(u'Campo a exibir')
        verbose_name_plural = _(u'Campos à exibir')
        ordering = ['position']


class QueryFilter(FieldModel):
    '''
    QueryFilter of a Queryset
    '''

    LOOKUPS = mapping.LOOKUPS
    FILTER_METHODS = (
        ('filter', _(u'Filtro')),
        ('exclude', _(u'Exclusão')),
    )

    lookup = models.CharField(
        _(u'Tipo de filtro'), max_length=max([len(x[0]) for x in LOOKUPS]),
        choices=LOOKUPS)
    method = models.CharField(
        _(u'Método'), choices=FILTER_METHODS,
        max_length=max([len(x[0]) for x in FILTER_METHODS])
    )
    readonly = models.BooleanField(default=False)
    value_0 = models.CharField(_(u'Valor padrão 1'), **_CNULL)
    value_1 = models.CharField(_(u'Valor padrão 2'), **_CNULL)

    def __str__(self):
        return '%s por %s' % (self.field_verbose, self.get_lookup_display())

    @property
    def lookup_config(self):
        lookup_info = mapping.LOOKUP_MAPPING[self.field_type]
        if self.lookup:
            lookup_config = lookup_info.get(self.lookup)
        else:
            lookup_config = None
        # returns something like
        # [('numerical-field', 0), ('numerical-field', 1)] or None
        return [
            (lookup_config[1], x) for x in range(lookup_config[0])
        ] if lookup_config else None

    class Meta:
        verbose_name = _(u'Filtro de query')
        verbose_name_plural = _(u'Filtros de query`s')
