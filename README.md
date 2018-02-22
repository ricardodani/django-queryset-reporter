Django Queryset Reporter
=================

Description
-----------

A django pluggable admin-site app for create persisted queryset's and make reports based on them, in various forms of data like cvs's, xlsx's.

Project URL: https://github.com/ricardodani/django-queryset-reporter/

Install
-------

Type:

```bash
   python setup.py install
```

In your **settings** add:

```python
  INSTALLED_APPS += ['queryset_reporter']

  #This variable represent how depth we will go into the models to set the fields as searchable fields. Default is 2.
  QUERY_SET_REPORT_MAX_RECURSIVE_DEPTH = 3
```

Migrate (if you`re using south):

```bash
./manage.py migrate queryset_reporter
```

Or (if not south):

```bash
./manage.py syncdb queryset_reporter
```

Add url's definitions to your **project.urls** module:

```python
#Queryset reporter urls
url(r'^', include('queryset_reporter.urls')),
```

Adding grappelli dashboard to your admin site
---------------------------------------------

To enable the dashboard of **queryset_reporter** in the home of admin, you must add grappelli-dashboard app in your **settings** *(Note: that must be after 'grappelli')*:

```python
INSTALED_APPS += ['grappelli.dashboard',]
```

Create a grappelli_dashboard.py to your project like this::
```python
# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import modules, Dashboard
from queryset_reporter.grappelli_dashboard import queryset_reporter_module

class CustomAdminDashboard(Dashboard):
    def init_with_context(self, context):
        # example to append a module of your app
        self.children.append(modules.AppList(
            title=_(u'Administração'),
            column=1,
            collapsible=True,
            css_classes=('collapse closed',),
            models=('django.contrib.*',),
        ))
        # TODO: append here all modules.Applist of your project

        # Append the queryset_reporter_module object
        self.children.append(queryset_reporter_module)

        self.children.append(modules.RecentActions(
            _(u'Ações Recentes'),
            limit=10,
            collapsible=False,
            column=2,
        ))
```
And then, in your **settings**:
```python
# GRAPELLI DASHBOARD
GRAPPELLI_INDEX_DASHBOARD = {
    'django.contrib.admin.site': 'your_project.grappelli_dashboard.CustomAdminDashboard',
}
```

To .csv generation works, you MUST define your **MEDIA_ROOT** and **MEDIA_URL** settings directives.

Configure some settings variables:

```python
# Default: Django Queryset Reporter
QR_TITLE = u'Default Title (big)'

# Default: Queryset Reporter
QR_HEADER_TITLE = u'Title'

# Default: https://github.com/ricardodani/django-queryset-reporter
QR_FOOTER_LINK = u'http://footer.link/'
````

Tested on
---------

- django == 1.4.22
- django-grappelli==2.3.9 (i don't know if works without grappelli, but I think it works)

About
-----

- Author: Ricardo Dani
- E-mail: ricardod@horizonte.tv.br / ricardodani@gmail.com
- Github: github.com/ricardodani
- Company: Horizonte Conteúdos - Rio de Janeiro / RJ
- Collaborators:
	- Marcos Cardoso ( mcardoso@horizonte.tv.br / vrcmarcos@gmail.com )

License
-------

GPL