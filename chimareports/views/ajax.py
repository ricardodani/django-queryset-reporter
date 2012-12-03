# -*- encoding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.utils.simplejson import dumps
from django.contrib.contenttypes.models import ContentType


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
    else:
        model = ctype.model_class()

    # thank`s for https://github.com/burke-software/django-report-builder
    _all_fields = [
        model._meta.get_field_by_name(x)
        for x in model._meta.get_all_field_names()]
    # fields ForeignKey or M2M, direct or not
    related_fields = [
        x for x in _all_fields
        if x[3] or not x[2] or hasattr(x[0], 'related')]
    # only direct fields
    direct_fields = [
        x for x in _all_fields
        if x[2] and not x[3] and x[0].__class__.__name__ != 'ForeignKey']

    #0[(<django.db.models.fields.related.ManyToManyField at 0x10e333490>, None, True, True),
    #1(<RelatedObject: tplay:banner related to filme>, None, False, False),
    #2(<django.db.models.fields.files.ImageField at 0x10e333690>, None, True, False),
    #3(<django.db.models.fields.DateTimeField at 0x10e33d390>, None, True, False),
    #4(<django.db.models.fields.DateTimeField at 0x10e33d350>, None, True, False),
    #5(<django.db.models.fields.related.ManyToManyField at 0x10e333590>, None, True, True),
    #6(<RelatedObject: tplay:especial related to filmes>, None, False, True),
    #7(<RelatedObject: tplay:filmeespecial related to filme>, None, False, False),
    #8(<RelatedObject: tplay:filmetrilho related to filme>, None, False, False),
    #9(<django.db.models.fields.AutoField at 0x10e333850>, None, True, False),
    #10(<django.db.models.fields.IntegerField at 0x10e333190>, None, True, False),
    #11(<django.db.models.fields.TextField at 0x10e333450>, None, True, False),
    #12(<django.db.models.fields.BooleanField at 0x10e333410>, None, True, False),
    #13(<django.db.models.fields.SlugField at 0x10e333390>, None, True, False),
    #14(<django.db.models.fields.CharField at 0x10e3331d0>, None, True, False),
    #15(<django.db.models.fields.CharField at 0x10e333310>, None, True, False),
    #16(<django.db.models.fields.DateTimeField at 0x10e333710>, None, True, False),
    #17(<RelatedObject: tplay_auth:usuariofilme related to filme>, None, False, False),
    #18(<django.db.models.fields.PositiveIntegerField at 0x10e3336d0>, None, True, False)]

    return json_response({
        'related_fields': related_fields,
        'direct_fields': direct_fields
    })
