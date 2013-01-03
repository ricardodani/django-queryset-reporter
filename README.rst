queryset_reporter
=================

Description
-----------

A django pluggable admin-site app for create persisted queryset`s and make reports based on them, in various forms of data like cvs`s, xlsx`s.

Url: https://github.com/ricardodani/django-queryset-reporter/

Install
-------

Type::

   python setup.py install

In your settings.INSTALLED_APPS add::

  queryset_reporter

Migrate (if you`re using south)::

  ./manage.py migrate queryset_reporter

Or (if not south)::

  ./manage.py syncdb queryset_reporter

Add url`s definitions to your project.urls module::

    # Queryset reporter
    url(r'^', include('queryset_reporter.urls')),

Adding grappelli dashboard to your admin site
---------------------------------------------

To enable the dashboard of ``queryset_reporter`` in the home of admin, you must add grappelli-dashboard app in your settings.INSTALLED_APPS.
Note that must be after 'grappelli'::
    
    'grappelli.dashboard',

Create a grappelli_dashboard.py to your project like this::

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

            # append the queryset_reporter_module object
            self.children.append(queryset_reporter_module)

            self.children.append(modules.RecentActions(
                _(u'Ações Recentes'),
                limit=10,
                collapsible=False,
                column=2,
            ))

And then, in your settings::

    # GRAPELLI DASHBOARD
    GRAPPELLI_INDEX_DASHBOARD = {
        'django.contrib.admin.site': 'your_project.grappelli_dashboard.CustomAdminDashboard',
    }

To generation of .csv works, you must define your ``MEDIA_ROOT`` and ``MEDIA_URL`` settings directives.

Configure some settings variables::

    # Default: Django Queryset Reporter
    QR_TITLE = u'Default Title (big)'
    
    # Default: Queryset Reporter
    QR_HEADER_TITLE = u'Title'

    # Default: https://github.com/ricardodani/django-queryset-reporter
    QR_FOOTER_LINK = u'http://footer.link/' 

tested on
---------

- django >= 1.3.1 <= 1.3.4
- django-grappelli==2.3.9 (i don`t know if works without grappelli, but I think it works)

about
-----

- Author: Ricardo Dani
- E-mail: ricardod@horizonte.tv.br / ricardodani@gmail.com
- Github: github.com/ricardodani
- Company: Horizonte Conteúdos - Rio de Janeiro / RJ

license
-------

GPL
