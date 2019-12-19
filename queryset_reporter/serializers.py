from rest_framework import serializers
from queryset_reporter.models import Queryset, DisplayField, QueryFilter


class QuerysetResultSerializer(serializers.Serializer):
    '''
    Serializes a generic queryset according to the initialized `fields`
    parameter.
    '''

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields')
        super().__init__(*args, **kwargs)
        self._init_fields(fields)

    def _init_fields(self, fields):
        for field in fields:
        #     self.fields[name] = field_type(
        #         allow_null=True,
        #         allow_empty=True,
        #         child=serializers.CharField()
        #     )
        # for field in fields:
            if field['field'] in ('created_at', 'updated_at'):
                self.fields[field['field']] = serializers.DateTimeField(allow_null=True)
            else:
                self.fields[field['field']] = serializers.CharField(allow_null=True)


class QuerysetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queryset
        fields = (
            'id',
            'name',
            'model',
            'distinct',
            'created_at',
            'modified_at'
        )


class DisplayFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayField
        fields = (
            'field',
            'field_verbose',
            'field_type',
            'sort',
            'annotate',
            'position'
        )


class QueryFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryFilter
        fields = (
            'field',
            'field_verbose',
            'field_type',
            'lookup',
            'method',
            'readonly',
            'value_0',
            'value_1'
        )
