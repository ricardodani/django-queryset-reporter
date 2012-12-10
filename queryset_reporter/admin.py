# -*- encoding: utf-8 -*-

from django.contrib import admin
from queryset_reporter.models import Queryset, Filter, Exclude, DisplayField
from queryset_reporter.forms import DisplayFieldForm, FilterForm, ExcludeForm


class DisplayFieldInline(admin.TabularInline):
    model = DisplayField
    form = DisplayFieldForm
    extra = 0
    classes = ('collapse open',)
    inline_classes = ('collapse',)
    sortable_field_name = "position"
    fields = (
        'field', 'field_verbose', 'field_type', 'model_field', 'sort', 'annotate',
        'position'
    )


class FilterInline(admin.TabularInline):
    model = Filter
    form = FilterForm
    extra = 0
    classes = ('collapse open',)
    inline_classes = ('collapse',)
    fields = (
        'field', 'field_verbose', 'field_type', 'model_field', 'lookup',
    )


class ExcludeInline(admin.TabularInline):
    model = Exclude
    form = ExcludeForm
    extra = 0
    classes = ('collapse open',)
    inline_classes = ('collapse',)
    fields = (
        'field', 'field_verbose', 'field_type', 'model_field', 'lookup',
    )


class QuerysetAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'distinct', 'created_at', 'modified_at')
    list_filter = ('model', 'created_at', 'modified_at', 'distinct')
    inlines = (DisplayFieldInline, FilterInline, ExcludeInline)
    fieldsets = (
        ('Dados básicos', {
            'fields': ('name', 'desc', 'model', 'distinct')
        }),
    )

    class Media:
        js = ("queryset_reporter/admin.js",)

admin.site.register(Queryset, QuerysetAdmin)
