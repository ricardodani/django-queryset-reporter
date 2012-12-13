# -*- encoding: utf-8 -*-

import re
import os
import uuid
import codecs
import csv
from datetime import datetime
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from queryset_reporter.models import Queryset


class Reporter(object):
    '''
    Manipulates a ``queryset_reporter.models.Queryset`` model to
    obtain another queryset based on ``Queryset`` metadada.
    '''

    def __init__(self, queryset, request):
        if isinstance(queryset, Queryset):
            self.queryset = queryset
            self.request = request
            self._request_filters()
            self._prepare_vars()
            self._filters()
        else:
            raise Exception(_(u'Instância de Modelo de Queryset inválida.'))

    def _request_filters(self):
        # selected_filters.
        _rfilter = re.compile(r'^filter-([\d]+)$')
        self.filters = [
            {
                'filter': self.queryset.queryfilter_set.get(id=x),
                'values': [self.request.GET.get(y) for y in self.request.GET
                           if y.startswith('filter-%s-' % x)]
            } for x in [
                int(_rfilter.match(x).groups()[0])
                for x in self.request.GET if _rfilter.match(x)
            ]  # returns the id`s of ``Filters`` objects.
        ]  # returns a dict with key 'filter' equals the ``Filter`` object and
        #    the values of the related filter.

    def _prepare_vars(self):
        # rsq -> result queryset
        self.rqs = self.queryset.model.model_class().objects.all()
        # fields -> display fields
        self.fields = self.queryset.displayfield_set.all()

    @staticmethod
    def _clean_values(values, config):
        '''Return a pythonic value of the given list of values
        '''
        def _clean_val(value, field_type):
            if field_type == 'datetime-field':
                return datetime.strptime(value, '%d/%m/%Y %H:%M')
            elif field_type == 'boolean-field':
                if value == '1':
                    return True
                else:
                    return False
            elif field_type == 'char-field':
                return value
            elif field_type == 'numerical-list':
                return [int(x.strip()) for x in value.split(',') if x.strip()]
            elif field_type == 'char-list':
                return [x.strip() for x in value.split(',') if x.strip()]
            elif field_type == 'numerical-field':
                if '.' in value:
                    return float(value)
                else:
                    return int(value)
            else:
                return None

        cleaned_values = [_clean_val(values[x], config[x][0])
                          for x in range(len(values))]
        if len(cleaned_values) == 1:
            return cleaned_values[0]
        else:
            return cleaned_values

    def _filters(self):
        for f in self.filters:
            flookup = '__'.join((f['filter'].field, f['filter'].lookup))
            fvalues = self._clean_values(f['values'], f['filter'].lookup_config)
            if f['filter'].method == u'filter':
                # append filter method
                self.rqs = self.rqs.filter(**{flookup: fvalues})
            elif f['filter'].method == u'exclude':
                # append exclude method
                self.rqs = self.rqs.exclude(**{flookup: fvalues})

    def _fields_list(self):
        return [x.field for x in self.fields]

    def get_base_qs(self):
        # f-> field, s -> sort
        # if sort is 'desc' prepend a `-` in front of `f` string
        sort_field = lambda f, s: (u'-%s' % f) if s == u'desc' else f
        # order_by <- a list of order_by fields with order signals
        # i.e: ['title', '-creation_time']
        order_by = [
            sort_field(x.field, x.sort) for x in
            self.queryset.displayfield_set.filter(sort__isnull=False)
        ]
        return self.rqs.order_by(*order_by).values_list(*self._fields_list())

    def get_filters(self):
        filter_dict = dict([
            (x['filter'], x['values'])
            for x in self.filters if x['filter'].method == 'filter'
        ])
        return [
            (x, x.lookup_config, filter_dict.get(x))
            for x in self.queryset.queryfilter_set.filter(method='filter')
        ]

    def get_excludes(self):
        exclude_dict = dict([
            (x['filter'], x['values'])
            for x in self.filters if x['filter'].method == 'exclude'
        ])
        return [
            (x, x.lookup_config, exclude_dict.get(x))
            for x in self.queryset.queryfilter_set.filter(method='exclude')
        ]

    def preview(self, limit=50):
        return self.get_base_qs()[:limit]

    def render_csv(self):
        '''Render a .CSV and return the file_url.
        '''
        file_name = 'csvs/%s.csv' % uuid.uuid4().hex
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        with codecs.open(file_path, 'wb', 'utf-8') as csvfile:
            spamwriter = csv.writer(csvfile, strict=True)
            spamwriter.writerow([
                x.field_verbose for x in self.queryset.displayfield_set.all()
            ])
            for line in self.get_base_qs():
                spamwriter.writerow(line)
        file_url = settings.MEDIA_URL + file_name
        return file_url
