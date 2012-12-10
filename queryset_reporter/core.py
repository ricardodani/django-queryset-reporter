# -*- encoding: utf-8 -*-

from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from queryset_reporter.models import Queryset


class Reporter(object):
    '''
    Manipulates a ``queryset_reporter.models.Queryset`` model to
    obtain another queryset based on ``Queryset`` metadada.
    '''

    def __init__(self, queryset, filters=None):
        if isinstance(queryset, Queryset):
            self.queryset = queryset
            self.filters = filters
            self._prepare_vars()
            self._filters()
        else:
            raise Exception(_(u'Instância de Modelo de Queryset inválida.'))

    def _prepare_vars(self):
        # rsq -> result queryset
        self.rqs = self.queryset.model.model_class().objects.all()
        # fields -> display fields
        self.fields = self.queryset.displayfield_set.all()

    @staticmethod
    def _clean_values(values, config):
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
            else:
                if '.' in value:
                    return float(value)
                else:
                    return int(value)

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

    def _get_base_qs(self):
        return self.rqs.values_list(*self._fields_list())

    def preview(self, limit=50):
        return self._get_base_qs()[:limit]
