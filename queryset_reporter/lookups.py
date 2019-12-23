class Lookup:
    field_class_name = None

    def __init__(self, field_class_name):
        if not self.field_class_name:
            self.field_class_name = field_class_name

    def get_fields(self):
        if self.two_values:
            return (), ()
        return ()


class Exact(Lookup):
    code = 'exact'
    verbose_name = _(u'Termo exato')
    two_values = False
    many = False


class Iexact(Lookup):
    code = 'iexact'
    verbose_name = _(u'Termo exato (case-insensitivo)')
    two_values = False
    many = False


class Contains(Lookup):
    code = 'contains'
    verbose_name = _(u'Contém o termo')
    two_values = False
    many = False

class Icontains(Lookup):
    code = 'icontains'
    verbose_name = _(u'Contém o termo (case-insensitivo)')
    two_values = False
    many = False


class In(Lookup):
    code = 'in'
    verbose_name = _(u'Termo está na lista')
    two_values = False
    many = True


class Gt(Lookup):
    code = 'gt'
    verbose_name = _(u'Maior que')
    two_values = False
    many = False


class Gte(Lookup):
    code  = 'gte'
    verbose_name = _(u'Maior ou igual que')
    two_values = False
    many = False


class Lt(Lookup):
    code = 'lt'
    verbose_name = _(u'Menor que')
    two_values = False
    many = False


class Lte(Lookup):
    code  = 'lte'
    verbose_name = _(u'Menor ou igual que')
    two_values = False
    many = False


class Startswith(Lookup):
    code = 'startswith'
    verbose_name = _(u'Começa com')
    two_values = False
    many = False


class Istartswith(Lookup):
    code = 'istartswith'
    verbose_name = _(u'Começa com (case-insensitivo)')
    two_values = False
    many = False


class Endswith(Lookup):
    code = 'endswith'
    verbose_name = _(u'Termina com')
    two_values = False
    many = False


class Iendswith(Lookup):
    code = 'iendswith'
    verbose_name = _(u'Termina com (case-insensitivo)')
    two_values = False
    many = False


class Range(Lookup):
    code = 'range'
    verbose_name = _(u'Faixa/período')
    two_values = True
    many = False


class Year(Lookup):
    code = 'year'
    verbose_name = _(u'Ano específico')
    two_values = False
    many = False


class Month(Lookup):
    code = 'month'
    verbose_name = _(u'Mês específico')
    two_values = False
    many = False


class Day(Lookup):
    code = 'day'
    verbose_name = _(u'Dia específico.')
    two_values = False
    many = False


class Isnull(Lookup):
    code = 'isnull'
    verbose_name = _(u'É nulo?')
    two_values = False
    many = False
    field_class_name = 'BooleanField'


class Search(Lookup):
    code = 'search'
    verbose_name = _(u'Busca textual')
    two_values = False
    many = False


class Regex(Lookup):
    code = 'regex'
    verbose_name = _(u'Expressão regular')
    two_values = False
    many = False


class Iregex(Lookup):
    code = 'regex'
    verbose_name = _(u'Expressão regular (Case-insensitivo)')
    two_values = False
    many = False


NUMERICAL_LOOKUPS = {
    Exact, Iexact, In, Gt, Gte, Lt, Lte, Range, Isnull
}

CHAR_LOOKUPS = {
    Exact, Iexact, Contains, Icontains, In, Startswith, Istartswith, Endswith,
    Iendswith, Range, Isnull, Search, Regex, Iregex
}

DATETIME_LOOKUPS = {
    Exact, Iexact, Gt, Gte, Lt, Lte, Range, Year, Month, Day, Isnull
}

BOOLEAN_LOOKUPS = {
    Exact, Isnull
}

RELATED_LOOKUPS = {
    Exact, In, Isnull
}

LOOKUPS = {
    'exact': Exact,
    'iexact': Iexact,
    'contains': Contains,
    'icontains': Icontains,
    'in': In,
    'gt': Gt,
    'gte': Gte,
    'lt': Lt,
    'lte': Lte,
    'startswith': Startswith,
    'istartswith': Istartswith,
    'endswith': Endswith,
    'iendswith': Iendswith,
    'range': Range,
    'year': Year,
    'month': Month,
    'day': Day,
    'isnull': Isnull,
    'search': Search,
    'regex': Regex,
    'iregex': Iregex,
}


LOOKUP_MAPPING = {
    'BigIntegerField': NUMERICAL_LOOKUPS,
    'IntegerField': NUMERICAL_LOOKUPS,
    'DecimalField': NUMERICAL_LOOKUPS,
    'FloatField': NUMERICAL_LOOKUPS,
    'PositiveIntegerField': NUMERICAL_LOOKUPS,
    'PositiveSmallIntegerField': NUMERICAL_LOOKUPS,
    'SmallIntegerField': NUMERICAL_LOOKUPS,
    'AutoField': NUMERICAL_LOOKUPS,
    'RelatedObject': RELATED_LOOKUPS,
    'ManyToManyField': RELATED_LOOKU/PS,
    'ForeignKey': RELATED_LOOKUPS,
    'OneToOneField': RELATED_LOOKUPS,
    'SlugField': CHAR_FIELD,
    'CharField': CHAR_FIELD,
    'TextField': CHAR_FIELD,
    'EmailField': CHAR_FIELD,
    'FileField': CHAR_FIELD,
    'FilePathField': CHAR_FIELD,
    'ImageField': CHAR_FIELD,
    'IPAddressField': CHAR_FIELD,
    'URLField': CHAR_FIELD,
    'XMLField': CHAR_FIELD,
    'DateTimeField': DATETIME_FIELD,
    'DateField': DATETIME_FIELD,
    'TimeField': DATETIME_FIELD,
    'BooleanField': BOOLEAN_FIELD,
}

def get_field_lookup(field_class_name, lookup_name):
    try:
        lookups = LOOKUP_MAPPING[field_class_name]
    except:
        raise Exception('No field type match')

    if LOOKUPS[lookup_name] not in lookups:
        raise Exception('No lookup match for field type')

    Lookup = LOOKUPS[lookup_name]

    return Lookup(field_class_name)

