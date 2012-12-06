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

tested on
---------

- django==1.3.1
- django-grappelli==2.3.9 (i don`t know if works without grappelli, i think it works)

about
-----

- Author: Ricardo Dani
- E-mail: ricardod@horizonte.tv.br
- Github: github.com/ricardodani

license
-------

GPL