from django.db.models.fields.related import RelatedField
from django.conf import settings

_DEFAULT_RECURSION_DEPTH = 2
_MAX_RECURSION_DEPTH = getattr(
    settings, 'QUERYSET_REPORTER_MAX_RECURSION_DEPTH', _DEFAULT_RECURSION_DEPTH
)

def _direct_field(field, recursion_depth=0):

    field_metadata = {
        'name': field.name,
        'verbose': field.verbose_name.format('%s'),
        'type': field.__class__.__name__,
    }
    # verify if it`s a RelatedField
    if (isinstance(field, RelatedField) and
            recursion_depth > _MAX_RECURSION_DEPTH):
        return None
    elif isinstance(field, RelatedField):
        # means that the field is OneToOneField, ManyToMany or a ForeignKey
        field_metadata.update({
            'lookup_fields': get_model_fields(
                field.rel.to, recursion_depth=recursion_depth
            ),
        })
    return field_metadata


def _related_object(field, field_name, recursion_depth=0):
    # for a non direct fields
    assert field.__class__.__name__ == 'RelatedObject'
    related_object = {
        'name': field_name,
        'verbose': field_name,
        'type': field.__class__.__name__,
    }
    if recursion_depth <= _MAX_RECURSION_DEPTH:
        related_object.update({
            'lookup_fields': get_model_fields(
                field.field.model, recursion_depth=recursion_depth
            ),
        })
    return related_object


def field_meta(field, field_name, recursion_depth=0):
    '''
    Return the name of the field, your verbose name, your type and your lookup
    fields, if exist.
    '''

    # First verify if `field` is direct or no

    if field[2]:
        # If the field is direct, means that it can be a ForeigKey,
        # ManyToManyField or a <?>Field (? = Char, Integer, ...)
        return _direct_field(field[0], recursion_depth)
    #elif isinstance(field[0], RelatedObject):
    elif field[0].__class__.__name__ == 'RelatedObject':
        return _related_object(field[0], field_name, recursion_depth)
    else:
        None


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
    for field_name in model._meta.get_all_field_names():
        # print '\t' * (recursion_depth - 1), 'field_name', field_name, 'recusion_depth', recursion_depth
        # get_field_by_name(field_name) -> Returns the (field_object, model,
        # direct, m2m), where field_object is the Field instance for the given
        # name, model is the model containing this field (None for local
        # fields), direct is True if the field exists on this model, and m2m
        # is True for many-to-many relations. When 'direct' is False,
        # 'field_object' is the corresponding RelatedObject for this field
        # (since the field doesn't have an instance associated with it).
        field = model._meta.get_field_by_name(field_name)
        f = field_meta(field, field_name, recursion_depth)
        if f:
            fields.append(f)
    return fields
