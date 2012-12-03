# -*- encoding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.utils.simplejson import dumps
from django.contrib.contenttypes.models import ContentType
from queryset_reporter.core import get_model_fields


def json_response(obj):
    '''Returns serialized json response based on a pythonic object
    (dict, str, tuple, list).
    '''
    return HttpResponse(dumps(obj), mimetype='application/json')


def model_fields(request):
    '''Returns a list of dicts that`s represents the fields metadata of an
    given model.
    '''

    # get`s the model from request.GET and return a error if doesn`t exist
    try:
        ctype = ContentType.objects.get(pk=request.GET.get('model'))
    except ContentType.DoesNotExist:
        return json_response({
            'success': False, 'error': _(u'Modelo inexiste.')})

    model = ctype.model_class()
    if not model:
        return json_response({
            'success': False, 'error': _(u'Modelo abstrato.')
        })

    return json_response({
        'success': True,
        'fields': get_model_fields(model),
    })
