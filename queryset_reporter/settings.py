from django.conf import settings as django_settings

'''
Defines the `app_labels` that will be excluded from model selection at
`Queryset` form. Empty list means no excluding.
'''
_QUERYSET_REPORTER_EXCLUDE_APPS_DEFAULT_VALUE = [
    'admin', 'contenttypes', 'sessions', 'queryset_reporter'
]
QUERYSET_REPORTER_EXCLUDE_APPS = getattr(
    django_settings,
    'QUERYSET_REPORTER_EXCLUDE_APPS',
    _QUERYSET_REPORTER_EXCLUDE_APPS_DEFAULT_VALUE
)

'''
Defines the `app_labels` that will be included exclusively in model field at
`Queryset` form. Emtpy list means no filtering.
'''
_QUERYSET_REPORTER_INCLUDE_APPS_DEFAULT_VALUE = []
QUERYSET_REPORTER_INCLUDE_APPS = getattr(
    django_settings,
    'QUERYSET_REPORTER_INCLUDE_APPS',
    _QUERYSET_REPORTER_INCLUDE_APPS_DEFAULT_VALUE
)


'''
Defaults to True, if False, `field`, `field_verbose`, `field_type` are
displayed in admin.
'''
QR_HIDE_FIELDS = getattr(
    django_settings, 'QR_HIDE_FIELDS', True
)
