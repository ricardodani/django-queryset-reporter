queryset_reporter
=================

description
-----------

A django pluggable admin-site app for create persisted queryset`s and then
make reports based on them in various forms of data like pdf`s, xls`s.

url: https://github.com/ricardodani/django-queryset-reporter/

install
-------

Type::

   python setup.py install

In your settings.INSTALLED_APPS add::

  queryset_reporter

migrate (with you`re using south)::

  ./manage.py migrate queryset_reporter

or (if not south)::

  ./manage.py syncdb queryset_reporter

add url`s definitions to your project.urls module::

    # Queryset reporter
    url(r'^', include('queryset_reporter.urls')),

add grappelli-dashboard app in your settings.INSTALLED_APPS. Note that must be after 'grappelli'::
    
    'grappelli.dashboard',

create a grappelli_dashboard.py to your project like this::

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

tested on
---------

- django==1.3.1
- django-grappelli==2.3.9 (i don`t know if works without grappelli, i think it works)

about
-----

- Author: Ricardo Dani
- E-mail: ricardod@horizonte.tv.br
- Github: github.com/ricardodani
- Company: Horizonte Conteúdos - Rio de Janeiro / RJ

license
-------

GPL
