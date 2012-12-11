# -*- encoding: utf-8 -*-

import re
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from queryset_reporter.models import Queryset
from queryset_reporter.core import Reporter


def create(request):
    '''
    View to create report`s.
    '''
    def render_page():
        return render(request, 'queryset_reporter/create.html', context)

    # all the querysets
    querysets = Queryset.objects.all()
    context = {
        'querysets': querysets,
    }

    try:
        qs = Queryset.objects.get(pk=request.GET.get('queryset'))
    except Queryset.DoesNotExist:
        return render_page()

    # selected_filters.
    _rfilter = re.compile(r'^filter-([\d]+)$')
    _filters_ids = [
        int(_rfilter.match(x).groups()[0])
        for x in request.GET if _rfilter.match(x)
    ]
    rep_filters = [
        {
            'filter': qs.queryfilter_set.get(id=x),
            'values': [request.GET.get(y) for y in request.GET
                       if y.startswith('filter-%s-' % x)]
        } for x in _filters_ids
    ]
    reporter = Reporter(qs, rep_filters)

    file_format = request.GET.get('format')
    if file_format == 'csv':
        context.update({
            'rendered_csv': reporter.render_csv()
        })

    context.update({
        'queryset': qs,
        #'checked_filters': filters_ids,
        'reporter': reporter,
        'display_fields': qs.displayfield_set.all(),
        'filters': qs.queryfilter_set.filter(method='filter'),
        'excludes': qs.queryfilter_set.filter(method='exclude'),
    })
    return render_page()
