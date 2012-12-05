# -*- encoding: utf-8 -*-

from django.db.models.fields.related import RelatedField
from django.db.models.related import RelatedObject


def _direct_field(field, only_normal=False):
    field_metadata = {
        'name': field.name,
        'verbose': field.verbose_name.format('%s'),
        'type': field.__class__.__name__,
    }
    # verify if it`s a RelatedField
    if isinstance(field, RelatedField) and only_normal:
        return None
    elif isinstance(field, RelatedField):
        # means that the field is OneToOneField, ManyToMany or a ForeignKey
        field_metadata.update({
            'lookup_fields': get_model_fields(field.rel.to, only_normal=True),
        })
    return field_metadata


def _related_object(field):
    # for a non direct fields
    return {
        'name': field.var_name,
        'verbose': field.model._meta.verbose_name_plural.format('%s'),
        'type': field.__class__.__name__,
        'lookup_fields': get_model_fields(
            field.field.model, only_normal=True),
    }


def field_meta(field, only_normal=False):
    '''
    Return the name of the field, your verbose name, your type and your lookup
    fields, if exist and if `only_normal` is False.
    '''

    # First verify if `field` is direct or no

    if field[2]:
        # If the field is direct, means that it can be a ForeigKey,
        # ManyToManyField or a <?>Field (? = Char, Integer, ...)
        return _direct_field(field[0], only_normal)
    elif isinstance(field[0], RelatedObject) and not only_normal:
        return _related_object(field[0])
    else:
        None


def get_model_fields(model, only_normal=False):
    '''
    Makes a instrospection in the fields of an given model and return all the
    fields with attribute name, verbose name and type.
    For related fields, like ForeignKey, ManyToManyField, OneToOneField and
    not direct fields, return them into key `lookup_fields`, and, for each of
    them, call this function again, but with `only_normal`=True, to certify
    a maximum of 1 level introspection.
    '''

    fields = []
    for field_name in model._meta.get_all_field_names():
        # get_field_by_name(field_name) -> Returns the (field_object, model,
        # direct, m2m), where field_object is the Field instance for the given
        # name, model is the model containing this field (None for local
        # fields), direct is True if the field exists on this model, and m2m
        # is True for many-to-many relations. When 'direct' is False,
        # 'field_object' is the corresponding RelatedObject for this field
        # (since the field doesn't have an instance associated with it).
        field = model._meta.get_field_by_name(field_name)
        f = field_meta(field, only_normal)
        if f:
            fields.append(f)
    return fields
