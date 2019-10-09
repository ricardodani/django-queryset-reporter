from django.urls import path, reverse
from django.views.generic.base import RedirectView
from queryset_reporter.views.ajax import model_fields
from queryset_reporter.views.core import create


app_name = 'queryset_reporter'
urlpatterns = [
    path(
        'api/model-fields', model_fields, name='qr_api_modelfields'
    ),
    path(
        'create', create, name='qr_create'
    ),
    path(
        '', RedirectView.as_view(pattern_name='queryset_reporter:qr_create'),
        name='qr_index'
    ),
]
