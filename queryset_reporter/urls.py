from django.urls import path
from queryset_reporter.views.api import (
    QuerysetListCreateView,
    QuerysetResultView,
    QuerysetDetailView,
    DisplayFieldListCreateView,
    DisplayFieldRetrieveUpdateDestroyView,
    QueryFilterListCreateView,
    QueryFilterRetrieveUpdateDestroyView,
    ModelListView,
)
from queryset_reporter.views.core import index


app_name = 'queryset_reporter'
urlpatterns = [
    path(
        'api/querysets/',
        QuerysetListCreateView.as_view(),
        name='queryset_list'
    ),
    path(
        'api/querysets/models/',
        ModelListView.as_view(),
        name='models_list'
    ),
    path(
        'api/querysets/<int:queryset_id>/',
        QuerysetDetailView.as_view(),
        name='queryset_detail'
    ),
    path(
        'api/querysets/<int:queryset_id>/results/',
        QuerysetResultView.as_view(),
        name='queryset_results'
    ),
    path(
        'api/querysets/<int:queryset_id>/fields/',
        DisplayFieldListCreateView.as_view(),
        name='queryset_field_list'
    ),
    path(
        'api/querysets/<int:queryset_id>/fields/<int:filter_id>',
        DisplayFieldRetrieveUpdateDestroyView.as_view(),
        name='queryset_field_detail'
    ),
    path(
        'api/querysets/<int:queryset_id>/filters/',
        QueryFilterListCreateView.as_view(),
        name='queryset_filter_list'
    ),
    path(
        'api/querysets/<int:queryset_id>/filters/<int:filter_id>',
        QueryFilterRetrieveUpdateDestroyView.as_view(),
        name='queryset_filter_detail'
    ),
    path('', index, name='qr_index'),
]
