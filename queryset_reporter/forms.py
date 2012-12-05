# -*- encoding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from queryset_reporter.models import Filter, Exclude, DisplayField


class FieldedModelForm(forms.ModelForm):
    '''
    A model form that`s hidden field and field_verbose with a HiddenInput
    widget and add`s a `model_field` ChoiceField to the form.
    '''
    field = forms.CharField(required=True, widget=forms.HiddenInput(
        attrs={'class': 'instrospect-field'}
    ))
    field_verbose = forms.CharField(required=True, widget=forms.HiddenInput(
        attrs={'class': 'introspect-field_verbose'}
    ))
    model_field = forms.ChoiceField(
        label=_(u'Campo'), required=False,
        widget=forms.Select(attrs={'class': 'introspect-model_field'})
    )


class DisplayFieldForm(FieldedModelForm):
    position = forms.IntegerField(required=False, widget=forms.HiddenInput(
        attrs={'class': 'field'}
    ))

    class Meta:
        model = DisplayField


class FilterForm(FieldedModelForm):
    class Meta:
        model = Filter


class ExcludeForm(FieldedModelForm):
    class Meta:
        model = Exclude
