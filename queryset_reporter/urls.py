# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from queryset_reporter.views.ajax import model_fields

urlpatterns = patterns(
    '',
    # AJAX VIEWS
    url(
        r'^queryset_reporter/ajax/model-fields/$',
        model_fields, name='ajax-model-fields'
    ),

)
