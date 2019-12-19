from django.urls import path
from queryset_reporter.views.api import (
    QuerysetListCreateView,
    QuerysetResultView,
    QuerysetRetrieveUpdateDestroyView,
    DisplayFieldListCreateView,
    DisplayFieldRetrieveUpdateDestroyView,
    QueryFilterListCreateView,
    QueryFilterRetrieveUpdateDestroyView
)
from queryset_reporter.views.core import index


urlpatterns = [
    path(
        'api/querysets/',
        QuerysetListCreateView.as_view()
    ),
    path(
        'api/querysets/<int:queryset_id>/',
        QuerysetRetrieveUpdateDestroyView.as_view()
    ),
    path(
        'api/querysets/<int:queryset_id>/results/',
        QuerysetResultView.as_view()
    ),
    path(
        'api/querysets/<int:queryset_id>/fields/',
        DisplayFieldListCreateView.as_view()
    ),
    path(
        'api/querysets/<int:queryset_id>/fields/<int:filter_id>',
        DisplayFieldRetrieveUpdateDestroyView.as_view()
    ),
    path(
        'api/querysets/<int:queryset_id>/filters/',
        QueryFilterListCreateView.as_view()
    ),
    path(
        'api/querysets/<int:queryset_id>/filters/<int:filter_id>',
        QueryFilterRetrieveUpdateDestroyView.as_view()
    ),
    path('', index, name='qr_index'),
]
