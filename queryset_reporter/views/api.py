from rest_framework import (
    permissions, generics, views, exceptions, response
)
from queryset_reporter.models import (
    Queryset, DisplayField, QueryFilter, ModelManager
)
from queryset_reporter.serializers import (
    QuerysetSerializer, DisplayFieldSerializer,
    QueryFilterSerializer, QuerysetResultSerializer,
    ContentTypeSerializer
)
from queryset_reporter.core import Reporter


class AuthenticatedMixin:
    permissions_classes = [permissions.IsAuthenticated]

class QuerysetListCreateView(generics.ListCreateAPIView, AuthenticatedMixin):
    queryset = Queryset.objects.all()
    serializer_class = QuerysetSerializer


class QuerysetRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView, AuthenticatedMixin
):
    queryset = Queryset.objects.all()
    serializer_class = QuerysetSerializer
    lookup_url_kwarg = 'queryset_id'



class QuerysetResultView(views.APIView, AuthenticatedMixin):

    def get_model_queryset(self, id_):
        try:
            return Queryset.objects.get(id=id_)
        except Queryset.DoesNotExist:
            raise exceptions.NotFound

    def get(self, request, *args, **kwargs):
        #filters = self.request.GET['filters']
        model_queryset = self.get_model_queryset(kwargs['queryset_id'])
        queryset = Reporter(model_queryset, self.request).get_queryset()
        #queryset = Reporter(model_queryset, filters).get_queryset()
        fields = model_queryset.get_fields()
        result_serializer = QuerysetResultSerializer(
            fields=fields,
            data=list(queryset),
            many=True
        )
        result_serializer.is_valid(raise_exception=True)
        return response.Response(dict(
            result=result_serializer.data,
            fields=fields,
        ))


class BaseQuerysetMixin:
    queryset_url_kwarg = 'queryset_id'
    def get_queryset(self, *args, **kwargs):
        return self._queryset.filter(
            queryset=self.kwargs[self.queryset_url_kwarg]
        )


class DisplayFieldListCreateView(
    BaseQuerysetMixin, AuthenticatedMixin, generics.ListCreateAPIView
):
    _queryset = DisplayField.objects.all()
    serializer_class = DisplayFieldSerializer


class DisplayFieldRetrieveUpdateDestroyView(
    BaseQuerysetMixin, AuthenticatedMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    _queryset = DisplayField.objects.all()
    serializer_class = DisplayFieldSerializer
    lookup_url_kwarg = 'field_id'


class QueryFilterListCreateView(
    BaseQuerysetMixin, AuthenticatedMixin, generics.ListCreateAPIView
):
    _queryset = QueryFilter.objects.all()
    serializer_class = QueryFilterSerializer


class QueryFilterRetrieveUpdateDestroyView(
    BaseQuerysetMixin, AuthenticatedMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    _queryset = QueryFilter.objects.all()
    serializer_class = QueryFilterSerializer
    lookup_url_kwarg = 'filter_id'


class ModelListView(generics.ListAPIView, AuthenticatedMixin):
    queryset = ModelManager.get_allowed_models().order_by('model')
    serializer_class = ContentTypeSerializer
