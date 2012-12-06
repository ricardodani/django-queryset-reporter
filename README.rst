queryset_reporter
=================

description
-----------

A django pluggable admin-site app for create persisted queryset`s and then
make reports based on them in various forms of data like pdf`s, xls`s.

install
-------

Type::

   python setup.py install

usage
-----

In your settings.INSTALLED_APPS add::

  queryset_reporter

syncdb or migrate (with south)::

  ./manage.py migrate queryset_reporter

or::

  ./manage.py syncdb queryset_reporter

about
-----

- Author: Ricardo Dani
- E-mail: ricardod@horizonte.tv.br
- Github: github.com/ricardodani

license
-------

GPL