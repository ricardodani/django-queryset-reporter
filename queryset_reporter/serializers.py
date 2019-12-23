from rest_framework import serializers
from queryset_reporter.models import Queryset, DisplayField, QueryFilter


class QuerysetResultSerializer(serializers.Serializer):
    '''
    Serializes a generic queryset according to the initialized `fields`
    parameter.
    '''

    _fieldtypes = {
        'CharField': (
            serializers.CharField, {'allow_null': True}
        ),
        'DateTimeField': (
            serializers.DateTimeField, {'allow_null': True}
        ),

        # django fields
        # AutoField
        # BigAutoField
        # BigIntegerField
        # BinaryField
        # BooleanField
        # CharField
        # DateField
        # DateTimeField
        # DecimalField
        # DurationField
        # EmailField
        # FileField
        # FileField
        # FieldFile
        # FilePathField
        # FloatField
        # ImageField
        # IntegerField
        # GenericIPAddressField
        # NullBooleanField
        # PositiveIntegerField
        # PositiveSmallIntegerField
        # SlugField
        # SmallAutoField
        # SmallIntegerField
        # TextField
        # TimeField
        # URLField
        # UUIDField

        # rest framework fields
        # Serializer fields
        # Core arguments
        # Boolean fields
        # BooleanField
        # NullBooleanField
        # String fields
        # CharField
        # EmailField
        # RegexField
        # SlugField
        # URLField
        # UUIDField
        # FilePathField
        # IPAddressField
        # Numeric fields
        # IntegerField
        # FloatField
        # DecimalField
        # Date and time fields
        # DateTimeField
        # DateField
        # TimeField
        # DurationField
        # Choice selection fields
        # ChoiceField
        # MultipleChoiceField
        # File upload fields
        # Parsers and file uploads.
        # FileField
        # ImageField
        # Composite fields
        # ListField
        # DictField
        # HStoreField
        # JSONField
        # Miscellaneous fields
        # ReadOnlyField
        # HiddenField
        # ModelField
        # SerializerMethodField
        #     self.fields[name] = field_type(
        #         allow_null=True,
        #         allow_empty=True,
        #         child=serializers.CharField()
        #     )
    }

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields')
        super().__init__(*args, **kwargs)
        self._init_fields(fields)

    def _get_serializer_field(self, field_name):
        field_class, field_kwargs = self._fieldtypes[field_name]
        return field_class(**field_kwargs)

    def _set_field(self, field):
        self.fields[field['field']] = self._get_serializer_field(
            field['field_type']
        )

    def _init_fields(self, fields):
        for field in fields:
            self._set_field(field)


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
