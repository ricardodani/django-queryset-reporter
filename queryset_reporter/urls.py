# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

from queryset_reporter.views.ajax import model_fields
from queryset_reporter.views.core import create

urlpatterns = patterns(
    '',
    # AJAX VIEWS
    url(
        r'^queryset_reporter/ajax/model-fields/$',
        model_fields, name='qsr_ajax-model-fields'
    ),
    url(
        r'^queryset_reporter/create/$',
        create, name='qsr_create'
    ),

)
