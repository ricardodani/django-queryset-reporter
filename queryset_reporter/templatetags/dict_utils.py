from django import template

register = template.Library()


@register.filter()
def get(d, key):
    try:
        return d.get(key)
    except AttributeError:
        return d