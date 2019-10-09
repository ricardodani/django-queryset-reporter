from django.contrib import admin
from queryset_reporter.models import Queryset, QueryFilter, DisplayField
from queryset_reporter.forms import DisplayFieldForm, QueryFilterForm


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


class QueryFilterInline(admin.TabularInline):
    model = QueryFilter
    form = QueryFilterForm
    extra = 0
    classes = ('collapse open',)
    inline_classes = ('collapse',)


class QuerysetAdmin(admin.ModelAdmin):
    change_form_template = 'admin/queryset_reporter_change_form.html'
    list_display = ('name', 'model', 'distinct', 'created_at', 'modified_at',
        'automatic_generation', 'last_automatic_generation_at')
    list_filter = ('model', 'created_at', 'modified_at', 'distinct',
        'automatic_generation')
    inlines = (DisplayFieldInline, QueryFilterInline)
    fields = ('name', 'desc', 'model', 'distinct', 'automatic_generation')

    class Media:
        js = (
            "queryset_reporter/admin.js",
            "https://code.jquery.com/jquery-1.4.4.min.js"
        )
        css = {
            'all': ("queryset_reporter/admin.css",)
        }

admin.site.register(Queryset, QuerysetAdmin)
