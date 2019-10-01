from django.conf import settings
from django.db.models.fields.reverse_related import ManyToOneRel

_DEFAULT_RECURSION_DEPTH = 2
_MAX_RECURSION_DEPTH = getattr(
    settings, 'QUERYSET_REPORTER_MAX_RECURSION_DEPTH', _DEFAULT_RECURSION_DEPTH
)


# (Pdb) model._meta.related_objects
# (<ManyToOneRel: animals.animal>,)
# HAS_LOOKUP_FIELDS = (ManyToOneRel)

def field_meta(field, field_name, recursion_depth=0):
    '''
    Return the name of the field, your verbose name, your type and your lookup
    fields, if exist.
    '''

    try:
        verbose_name = field.verbose_name
    except AttributeError: # ManyToOneRel
        verbose_name = field.name.capitalize()

    related_object = {
        'name': field_name,
        'verbose': verbose_name,
        'type': str(type(field)),
    }
    if (
        recursion_depth <= _MAX_RECURSION_DEPTH and
        isinstance(field, ManyToOneRel)
    ):
        related_object.update({
            'lookup_fields': get_model_fields(
                field.field.model, recursion_depth=recursion_depth
            ),
        })
    return related_object

def get_model_fields(model, recursion_depth=0):
    '''
    Makes a instrospection in the fields of an given model and return all the
    fields with attribute name, verbose name and type.
    For related fields, like ForeignKey, ManyToManyField, OneToOneField and
    not direct fields, return them into key `lookup_fields`, and, for each of
    them, call this function again, respecting the `_MAX_RECURSION_DEPTH` conf.
    '''

    fields = []
    recursion_depth += 1

    breakpoint()
    for field in model._meta.get_fields():
        f = field_meta(field, recursion_depth)
        if f:
            fields.append(f)
    return fields
