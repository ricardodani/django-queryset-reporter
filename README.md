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
pip install queryset_reporter
```

In your **settings** add:

```python
INSTALLED_APPS += ['queryset_reporter']
```

Migrate `queryset_reporter`` tables:

```bash
./manage.py migrate
```


Add url's definitions to your **project.urls** module:

```python
path('qr/', include('queryset_reporter.urls')),
```

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

- django == 2.2.x
- python == 3.7.x

About
-----

- Author: Ricardo Dani
- E-mail: ricardodani@gmail.com
- Github: github.com/ricardodani

License
-------

GPL
