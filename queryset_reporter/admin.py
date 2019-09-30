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
        'field', 'field_verbose', 'field_type', 'model_field', 'sort',
        'annotate', 'position', 'pre_concatenate', 'pos_concatenate'
    )


class FilterInline(admin.TabularInline):
    model = Filter
    form = FilterForm
    extra = 0
    classes = ('collapse open',)
    inline_classes = ('collapse',)
    fields = (
        'field', 'field_verbose', 'field_type', 'model_field', 'lookup',
        'readonly', 'value_0', 'value_1'
    )


class ExcludeInline(admin.TabularInline):
    model = Exclude
    form = ExcludeForm
    extra = 0
    classes = ('collapse open',)
    inline_classes = ('collapse',)
    fields = (
        'field', 'field_verbose', 'field_type', 'model_field', 'lookup',
        'readonly', 'value_0', 'value_1'
    )


class QuerysetAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'distinct', 'created_at', 'modified_at',
        'automatic_generation', 'last_automatic_generation_at')
    list_filter = ('model', 'created_at', 'modified_at', 'distinct',
        'automatic_generation')
    inlines = (DisplayFieldInline, FilterInline, ExcludeInline)
    fieldsets = (
        ('Dados básicos', {
            'fields': ('name', 'desc', 'model', 'distinct',
                'automatic_generation')
        }),
    )

    class Media:
        js = ("queryset_reporter/admin.js",)
        css = {
            'all': ("queryset_reporter/admin.css",)
        }

admin.site.register(Queryset, QuerysetAdmin)
