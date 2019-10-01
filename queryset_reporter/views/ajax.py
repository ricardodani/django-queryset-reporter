from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.utils.translation import ugettext as _
from queryset_reporter.introspect import get_model_fields


@permission_required('is_staff')
def model_fields(request):
    '''Returns a list of dicts that`s represents the fields metadata of an
    given model.
    '''

    # get`s the model from request.GET and return a error if doesn`t exist
    try:
        ctype = ContentType.objects.get(pk=request.GET.get('model'))
    except ContentType.DoesNotExist:
        return JsonResponse({
            'success': False, 'error': _(u'Modelo inexiste.')})
    except ValueError:
        return JsonResponse({
            'success': False, 'error': _(u'Identificador do modelo inválido')})

    model = ctype.model_class()
    if not model:
        return JsonResponse({
            'success': False, 'error': _(u'Modelo abstrato.')
        })

    return JsonResponse({
        'success': True,
        'model': str(model),
        'model_verbose': model._meta.verbose_name.format('%s'),
        'fields': get_model_fields(model),
    })
