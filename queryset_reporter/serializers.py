from rest_framework import serializers
from queryset_reporter.models import Queryset


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
