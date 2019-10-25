import re
import os
import uuid
from datetime import datetime

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db.models import aggregates
from openpyxl import Workbook

from queryset_reporter.models import Queryset, QueryFilter


class Reporter(object):
    '''
    Manipulates a ``queryset_reporter.models.Queryset`` model to
    obtain another queryset based on ``Queryset`` metadada.
    '''

    def __init__(self, queryset, request=None):
        if isinstance(queryset, Queryset):
            self.queryset = queryset
            self.request = request
            self._request_filters()
            self._prepare_vars()
            self._filters()
        else:
            raise Exception(_('Instância de Modelo de Queryset inválida.'))

    def _request_filters(self):
        self.filters = []
        # get readonly filters
        for rof in self.queryset.queryfilter_set.filter(readonly=True):
            f = {'filter': rof}
            if rof.value_1:
                f.update({'values': [rof.value_0, rof.value_1]})
                self.filters.append(f)
            elif rof.value_0:
                f.update({'values': [rof.value_0]})
                self.filters.append(f)

        # returns the id`s of ``Filters`` objects of the request GET.
        if self.request:
            filter_ids = []
            _rfilter = re.compile(r'^filter-([\d]+)$')
            for x in self.request.GET:
                match = _rfilter.match(x)
                if match:
                    filter_ids.append(int(match.groups()[0]))

            # appends to self.filter a dict with key 'filter' equals the
            # ``Filter`` object and the values of the related filter.
            for fid in filter_ids:
                try:
                    _filter = self.queryset.queryfilter_set.get(id=fid)
                except QueryFilter.DoesNotExist:
                    continue
                if _filter not in [x['filter'] for x in self.filters]:
                    self.filters.append({
                        'filter': _filter,
                        'values': [
                            self.request.GET.get(v)
                            for v in sorted(self.request.GET)
                            if v.startswith('filter-%s-' % fid)
                        ]
                    })

    def _prepare_vars(self):
        # rsq -> result queryset
        model_class = self.queryset.model.model_class()
        self._rqs = model_class.objects.all()
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
                self._rqs = self._rqs.filter(**{flookup: fvalues})
            elif f['filter'].method == u'exclude':
                # append exclude method
                self._rqs = self._rqs.exclude(**{flookup: fvalues})
        if self.queryset.distinct:
            self._rqs = self._rqs.distinct()

    def _fields_list(self):
        fields_list = []
        for f in self.fields:
            if not f.annotate:
                fields_list.append(f.field)
        return fields_list

    def _order_by(self):
        # f-> field, s -> sort
        # if sort is 'desc' prepend a `-` in front of `f` string
        sort_field = lambda f, s: (u'-%s' % f) if s == u'desc' else f
        # order_by <- a list of order_by fields with order signals
        # i.e: ['title', '-creation_time']
        return [
            sort_field((
                x.field if not x.annotate
                else ('%s_%s' % (x.annotate, x.field)).replace('__', '_')
            ), x.sort) for x in
            self.queryset.displayfield_set.filter(sort__isnull=False)
        ]

    def _annotate_dict(self):
        annot_list = []
        for x in self.queryset.displayfield_set.filter(annotate__isnull=False):
            key = ('%s_%s' % (x.annotate, x.field)).replace('__', '_')
            try:
                agg_class = getattr(aggregates, x.annotate)
            except AttributeError:
                continue
            else:
                annot_list.append([key, agg_class(x.field)])
        return dict(annot_list)

    def get_base_qs(self):
        order = self._order_by()
        fields = self._fields_list()
        annot = self._annotate_dict()
        if annot:
            return self._rqs.values(*fields).annotate(**annot).order_by(*order)
        else:
            return self._rqs.values(*fields).order_by(*order)

    def _get_queryfilters(self, method):
        '''
        Returns a list of ``queryfilter``s of the queryset with the kind of
        the given ``method`` (possible values is `filter` or `exclude`).
        '''
        if method not in ('filter', 'exclude'):
            raise Exception(
                'Invalid ``method`` argument, must be `filter` or `exclude`.'
            )
        filter_dict = dict([
            (x['filter'], x['values'])
            for x in self.filters if x['filter'].method == method
        ])
        return [
            (x, x.lookup_config, filter_dict.get(x))
            for x in self.queryset.queryfilter_set.filter(method=method)
        ]

    def get_filters(self):
        return self._get_queryfilters('filter')

    def get_excludes(self):
        return self._get_queryfilters('exclude')

    def preview(self, limit=50):
        return self.get_base_qs()[:limit]

    def count(self):
        return self.get_base_qs().count()

    def render_xlsx(self):
        wb = Workbook()
        ws = wb.create_sheet()

        ws.append(
            [x.field_verbose for x in self.queryset.displayfield_set.all()])
        for line in self.get_base_qs():
            _list = []
            for field in self.fields:
                pre_concat = (
                    field.pre_concatenate if field.pre_concatenate else ''
                )
                pos_concat = (
                    field.pos_concatenate if field.pos_concatenate else ''
                )
                line_value = line.get(field.get_field)
                _list.append(f'{pre_concat}{line_value}{pos_concat}')
            ws.append(_list)
        file_name = 'xlsx/%s.xlsx' % uuid.uuid4().hex
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        wb.save(file_path)

        return settings.MEDIA_URL + file_name
