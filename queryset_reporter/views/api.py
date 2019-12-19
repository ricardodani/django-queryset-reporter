from rest_framework import (
    permissions, generics, views, exceptions, response
)
from queryset_reporter.models import (
    Queryset, DisplayField, QueryFilter
)
from queryset_reporter.serializers import (
    QuerysetSerializer, DisplayFieldSerializer,
    QueryFilterSerializer, QuerysetResultSerializer
)
from queryset_reporter.core import Reporter


class QuerysetListCreateView(generics.ListCreateAPIView):
    queryset = Queryset.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = QuerysetSerializer


class QuerysetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Queryset.objects.all()
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = QuerysetSerializer
    lookup_url_kwarg = 'queryset_id'


class QuerysetResultView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            model_queryset = Queryset.objects.get(id=kwargs['queryset_id'])
        except Queryset.DoesNotExist:
            raise exceptions.NotFound
        queryset = Reporter(model_queryset, self.request).get_queryset()
        fields = model_queryset.get_fields()
        result_serializer = QuerysetResultSerializer(
            data=list(queryset),
            many=True,
            fields=model_queryset.get_fields()
        )
        result_serializer.is_valid(raise_exception=True)
        return response.Response(dict(
            result=result_serializer.data,
            fields=fields
        ))


class BaseQuerysetMixin:
    queryset_url_kwarg = 'queryset_id'
    def get_queryset(self, *args, **kwargs):
        return self._queryset.filter(
            queryset=kwargs[self.queryset_url_kwargs]
        )


class DisplayFieldListCreateView(
    generics.ListCreateAPIView, BaseQuerysetMixin
):
    _queryset = DisplayField.objects.all()
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = DisplayFieldSerializer


class DisplayFieldRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView, BaseQuerysetMixin
):
    _queryset = DisplayField.objects.all()
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = DisplayFieldSerializer
    lookup_url_kwarg = 'field_id'


class QueryFilterListCreateView(
    generics.ListCreateAPIView, BaseQuerysetMixin
):
    _queryset = QueryFilter.objects.all()
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = QueryFilterSerializer


class QueryFilterRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView, BaseQuerysetMixin
):
    _queryset = QueryFilter.objects.all()
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = QueryFilterSerializer
    lookup_url_kwarg = 'filter_id'
