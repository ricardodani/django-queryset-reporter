# -*- encoding: utf-8 -*-

'''
Models of queryset_reporter.
'''

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.contenttypes.models import ContentType

_NULL = {'null': True, 'blank': True}
_CHAR = {'max_length': 255}
_CNULL = _CHAR
_CNULL.update(_NULL)


class Queryset(models.Model):
    '''Queryset is a model representation of a generic Model.
    '''

    name = models.CharField(_(u'Nome'), **_CHAR)
    desc = models.TextField(_(u'Descrição'), **_CHAR)
    model = models.ForeignKey(ContentType, verbose_name=_(u'Modelo'))
    created_at = models.DateTimeField(_(u'Criação'), auto_now_add=True)
    modified_at = models.DateTimeField(_(u'Modificação'), auto_now=True)

    def __unicode__(self):
        return u'[%s] %s' % (self.model.name, self.name)

    class Meta:
        verbose_name = _(u'Queryset')
        verbose_name_plural = _(u'Querysets')


class FieldedModel(models.Model):
    queryset = models.ForeignKey(Queryset)
    field = models.CharField(_(u'Código do Campo'), **_CHAR)
    field_verbose = models.CharField(_(u'Nome do Campo'), **_CHAR)

    class Meta:
        abstract = True


class DisplayField(FieldedModel):
    '''Or the Fields and Extras selects called in .values().
    '''

    sort = models.CharField(
        verbose_name=_(u'Ordenação'), max_length=4, choices=(
            ('asc', _(u'Crescente')),
            ('desc', _('Decrescente'))
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

    def __unicode__(self):
        return u'%s por %s' % (self.field_verbose)

    class Meta:
        verbose_name = _(u'Campo a exibir')
        verbose_name_plural = _(u'Campos à exibir')
        ordering = ['position']

class QueryFilter(FieldedModel):
    '''
    QueryFilter of a Queryset
    '''

    LOOKUPS = (
        ('exact', _(u'Termo exato')),
        ('iexact', _(u'Termo exato (case-insensitivo)')),
        ('contains', _(u'Contém o termo')),
        ('icontains', _(u'Contém o termo (case-insensitivo)')),
        ('in', _(u'Termo está na lista')),
        ('gt', _(u'Maior que')),
        ('gte', _(u'Maior ou igual que')),
        ('lt', _(u'Menor que')),
        ('lte', _(u'Menor ou igual que')),
        ('startswith', _(u'Começa com')),
        ('istartswith', _(u'Começa com (case-insensitivo)')),
        ('endswith', _(u'Termina com')),
        ('iendswith', _(u'Termina com (case-insensitivo)')),
        ('range', _(u'Faixa/período')),
        ('year', _(u'Ano específico')),
        ('month', _(u'Mês específico')),
        ('day', _(u'Dia específico.')),
        ('isnull', _(u'É nulo?')),
        ('search', _(u'Busca textual')),  # mysql
        ('regex', _(u'Expressão regular')),
        ('iregex', _(u'Expressão regular (case-insensitivo)')),
    )
    FILTER_METHODS = (
        ('filter', _(u'Filtro')),
        ('exclude', _(u'Exclusão')),
    )

    lookup = models.CharField(
        _(u'Tipo de filtro'), max_length=max([len(x[0]) for x in LOOKUPS]),
        choices=LOOKUPS)
    value = models.CharField(_(u'Valor'), **_CHAR)
    value_2 = models.CharField(_(u'Valor opcicional'), **_CNULL)
    method = models.CharField(
        _(u'Método'), choices=FILTER_METHODS, editable=False,
        max_length=max([len(x[0]) for x in FILTER_METHODS]))

    def __unicode__(self):
        return u'%s por %s' % (self.field, self.get_lookup_display())

    class Meta:
        verbose_name = _(u'Filtro de query')
        verbose_name = _(u'Filtros de query`s')


class FilterManager(models.Manager):
    def get_query_set(self):
        qs = super(FilterManager, self).get_query_set()
        return qs.filter(method='filter')


class Filter(QueryFilter):
    '''
    Filter is a proxy model of QueryFilter to handle a .filter()
    '''

    objects = FilterManager()

    def __init__(self, *args, **kwargs):
        self.method = 'filter'
        super(Filter, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.method = 'filter'
        super(Filter, self).save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = _(u'Filtro Padrão')
        verbose_name_plural = _(u'Filtros Padrões')


class ExcludeManager(models.Manager):
    def get_query_set(self):
        qs = super(ExcludeManager, self).get_query_set()
        return qs.filter(method='exclude')


class Exclude(QueryFilter):
    '''
    Exclude is a proxy model of QueryFilter to handle a .exclude()
    '''

    objects = ExcludeManager()

    def __init__(self, *args, **kwargs):
        self.method = 'exclude'
        super(Exclude, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.method = 'exclude'
        super(Exclude, self).save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = _('Filtro de Exclusão')
        verbose_name_plural = _('Filtros de Exclusão')
