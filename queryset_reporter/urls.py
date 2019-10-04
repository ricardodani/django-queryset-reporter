from django.urls import path
from queryset_reporter.views.ajax import model_fields
from queryset_reporter.views.core import create


urlpatterns = [
    path(
        'ajax/model-fields', model_fields, name='qsr_ajax-model-fields'
    ),
    path(
        'create', create, name='qsr_create'
    ),
]
