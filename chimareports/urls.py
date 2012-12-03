# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from chimareports.views.ajax import model_fields

urlpatterns = patterns(
    '',
    # AJAX VIEWS
    url(
        r'^admin/queryset_reporter/ajax/model-fields/$',
        model_fields, name='ajax-model-fields'
    ),

)
