# -*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from grappelli.dashboard import modules, Dashboard

# TODO: make it a class inheriting LinkList
# bug: when i tried to do that, a template bug occours.
# TODO: use reverse url`s
queryset_reporter_module = modules.LinkList(
    _(u'Relatórios'),
    children=[
        {
            'title': _(u'Criar relatório'),
            'url': reverse('qsr_create'),
            'description': _(u'A partir de um modelo pré-existente, cria relatório.'),
        },
        (_(u'Criar modelos de relatórios'), reverse('admin:queryset_reporter_queryset_add')),
        (_(u'Administrar modelos de relatórios'), reverse('admin:queryset_reporter_queryset_changelist')),
    ],
    column=2
)


class CustomDashboard(Dashboard):
    '''
    Basic dashboard to use with grappelli to get util links from the
    dashboard.

    WARNING !!!

    Note that the direct use of this dashboard will result in a admin first
    page only with the queryset_reporter module. The ideal use of this is
    extending.
    '''

    def init_with_context(self, context):
        super(CustomDashboard, self).init_with_context(context)
        self.children.append(queryset_reporter_module)
