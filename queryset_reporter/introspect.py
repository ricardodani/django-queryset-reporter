from django.conf import settings
from django.db.models.fields import Field
from django.db.models.fields.reverse_related import ManyToOneRel, ManyToManyRel
from django.db.models.fields.related import ManyToManyField, ForeignKey

_DEFAULT_RECURSION_DEPTH = 2
_MAX_RECURSION_DEPTH = getattr(
    settings, 'QUERYSET_REPORTER_MAX_RECURSION_DEPTH', _DEFAULT_RECURSION_DEPTH
)


def get_class_name(object):
    return object.__class__.__name__


def _direct_field(field, recursion_depth=0):
    field_metadata = {
        'name': field.name,
        'verbose': field.verbose_name.format('%s'),
        'type': get_class_name(field)
    }
    if isinstance(field, (ManyToManyField, ForeignKey)):
        if recursion_depth > _MAX_RECURSION_DEPTH:
            return None

        field_metadata.update({
            'lookup_fields': get_model_fields(
                field.target_field.model, recursion_depth=recursion_depth
            )
        })
    return field_metadata


def _related_object(field, recursion_depth=0):
    related_object = {
        'name': field.name,
        'verbose': field.name.capitalize(),
        'type': get_class_name(field),
    }
    if recursion_depth <= _MAX_RECURSION_DEPTH:
        related_object.update({
            'lookup_fields': get_model_fields(
                field.field.model, recursion_depth=recursion_depth
            )
        })
    return related_object


def _field_meta(field, recursion_depth=0):
    '''
    Return the name of the field, your verbose name, your type and your lookup
    fields, if exist.
    '''

    if isinstance(field, (ManyToOneRel, ManyToManyRel)):
        return _related_object(field, recursion_depth)
    elif isinstance(field, Field):
        return _direct_field(field, recursion_depth)


def get_model_fields(model, recursion_depth=0):
    '''
    Make a instrospection in the fields of an given model and return all the
    fields with attribute name, verbose name and type.
    For related fields, like ForeignKey, ManyToManyField, OneToOneField and
    not direct fields, return them into key `lookup_fields`, and, for each of
    them, call this function again, respecting the `_MAX_RECURSION_DEPTH` conf.
    '''

    fields = []
    recursion_depth += 1

    for field in model._meta.get_fields():
        f = _field_meta(field, recursion_depth)
        if f:
            fields.append(f)
    return fields
