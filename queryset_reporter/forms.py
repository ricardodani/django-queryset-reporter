from django import forms
from django.utils.translation import ugettext_lazy as _

from queryset_reporter.models import DisplayField, QueryFilter
from queryset_reporter import settings


def get_widget_input(attrs):
    '''Returns a input widget for the "magic fields" of FieldModel
    based on project settings.
    '''
    if settings.QR_HIDE_FIELDS:
        return forms.HiddenInput(attrs=attrs)
    else:
        return forms.TextInput(attrs=attrs)


class FieldModelForm(forms.ModelForm):
    '''Customizes `field`, `field_verbose` and `field_type`; adds `model_type`
    '''

    field = forms.CharField(
        label=_(u'Nome do campo'), required=True,
        widget=get_widget_input(
            {'class': 'introspect-field', 'readonly': 'readonly'}
        )
    )

    field_verbose = forms.CharField(
        label=_(u'Apelido do campo'), required=True,
        widget=forms.TextInput(
            attrs={'class': 'introspect-field_verbose'}
        )
    )

    field_type = forms.CharField(
        label=_(u'Tipo do campo'), required=True,
        widget=get_widget_input(
            {'class': 'introspect-field_type', 'readonly': 'readonly'}
        )
    )

    model_field = forms.CharField(
        label=_(u'Buscar campo'), required=False,
        widget=forms.Select(
            attrs={'class': 'introspect-model_field'}
        )
    )


class DisplayFieldForm(FieldModelForm):
    position = forms.IntegerField(required=False, widget=forms.HiddenInput(
        attrs={'class': 'field'}
    ))

    class Meta:
        model = DisplayField
        fields = [
            'queryset', 'field', 'field_verbose', 'field_type', 'model_field',
            'sort', 'annotate', 'position', 'pre_concatenate', 'pos_concatenate'
        ]


class QueryFilterForm(FieldModelForm):
    class Meta:
        model = QueryFilter
        fields = [
            'queryset', 'field', 'field_verbose', 'field_type', 'model_field',
            'method', 'lookup', 'readonly', 'value_0', 'value_1'
        ]
