from django.contrib.auth.decorators import (
    permission_required, login_required
)
from django.shortcuts import render
from queryset_reporter.models import Queryset
from queryset_reporter.core import Reporter
from queryset_reporter import __version__ as version


@login_required
@permission_required('queryset_reporter.can_use_reports')
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
        'version': version,
    }

    try:
        qs = Queryset.objects.get(
            pk=request.GET.get('queryset')
        )
    except Queryset.DoesNotExist:
        return render_page()

    reporter = Reporter(qs, request)
    reporter.get_filters()

    file_format = request.GET.get('format')
    if file_format == 'csv':
        context.update({
            'rendered_csv': reporter.render_csv()
        })
    elif file_format == 'xlsx':
        context.update({
            'rendered_xlsx': reporter.render_xlsx()
        })

    context.update({
        'reporter': reporter,
        'request': request,
    })
    return render_page()
