# -*- encoding: utf-8 -*-

from django.contrib import admin
from chimareports.models import Queryset, Filter, Exclude, Order


class FilterInline(admin.StackedInline):
    model = Filter
    extra = 0
    classes = ('collapse open',)
    inline_classes = ('collapse',)


class ExcludeInline(admin.StackedInline):
    model = Exclude
    extra = 0
    classes = ('collapse open',)
    inline_classes = ('collapse',)


class OrderInline(admin.StackedInline):
    model = Order
    extra = 0
    classes = ('collapse open',)
    inline_classes = ('collapse',)


class QuerysetAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'model', 'created_at', 'modified_at')
    list_filter = ('model', 'created_at', 'modified_at')
    inlines = (FilterInline, ExcludeInline, OrderInline)

    class Midia:
        css = {
            "all": ("css/chimareports.css",)
        }
        js = ("js/chimareports.js",)

admin.site.register(Queryset, QuerysetAdmin)
