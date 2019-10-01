# -*- encoding: utf-8 -*-

from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from queryset_reporter.models import Filter, Exclude, DisplayField


# Defaults to True, if False, `fie1d`, `field_verbose`, `field_type` are
# displayed in admin.
QR_HIDE_FIELDS = getattr(settings, 'QR_HIDE_FIELDS', True)
if QR_HIDE_FIELDS:
    _widget = forms.HiddenInput
else:
    _widget = forms.TextInput


class FieldModelForm(forms.ModelForm):
    '''
    A ModelForm that hiddens `field and field_verbose with a HiddenInput
    widget and add`s a `model_field` ChoiceField to the form.
    '''

    field = forms.CharField(
        label=_(u'Nome do campo'), required=True,
        widget=_widget(attrs={'class': 'introspect-field', 'readonly': 'readonly'}))

    field_verbose = forms.CharField(
        label=_(u'Apelido do campo'), required=True,
        widget=_widget(attrs={'class': 'introspect-field_verbose'}))

    field_type = forms.CharField(
        label=_(u'Tipo do campo'), required=True,
        widget=_widget(attrs={'class': 'introspect-field_type', 'readonly': 'readonly'}))

    model_field = forms.CharField(
        label=_(u'Buscar campo'), required=False,
        widget=forms.Select(attrs={'class': 'introspect-model_field'}))


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


class FilterForm(FieldModelForm):
    class Meta:
        model = Filter
        fields = [
            'field', 'field_verbose', 'field_type', 'model_field', 'lookup',
            'readonly', 'value_0', 'value_1'
        ]


class ExcludeForm(FieldModelForm):
    class Meta:
        model = Exclude
        fields = [
            'field', 'field_verbose', 'field_type', 'model_field', 'lookup',
            'readonly', 'value_0', 'value_1'
        ]
