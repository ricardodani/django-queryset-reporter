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

    def get_model_queryset(self, id_):
        try:
            return Queryset.objects.get(id=id_)
        except Queryset.DoesNotExist:
            raise exceptions.NotFound

    def get(self, request, *args, **kwargs):
        model_queryset = self.get_model_queryset(kwargs['queryset_id'])
        queryset = Reporter(model_queryset, self.request).get_queryset()
        fields = model_queryset.get_fields()
        result_serializer = QuerysetResultSerializer(
            data=list(queryset),
            fields=fields,
            many=True,
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
            queryset=self.kwargs[self.queryset_url_kwarg]
        )


class DisplayFieldListCreateView(
    BaseQuerysetMixin,
    generics.ListCreateAPIView
):
    _queryset = DisplayField.objects.all()
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = DisplayFieldSerializer


class DisplayFieldRetrieveUpdateDestroyView(
    BaseQuerysetMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    _queryset = DisplayField.objects.all()
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = DisplayFieldSerializer
    lookup_url_kwarg = 'field_id'


class QueryFilterListCreateView(
    BaseQuerysetMixin, generics.ListCreateAPIView
):
    _queryset = QueryFilter.objects.all()
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = QueryFilterSerializer


class QueryFilterRetrieveUpdateDestroyView(
    BaseQuerysetMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    _queryset = QueryFilter.objects.all()
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = QueryFilterSerializer
    lookup_url_kwarg = 'filter_id'
