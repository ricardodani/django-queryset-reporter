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
INSTALLED_APPS = [
    # ...
    'queryset_reporter',
]
```

Migrate `queryset_reporter`` models:

```bash
./manage.py migrate
```


Add url's definitions to your **project.urls** module:

```python
path('path-of-choice/', include('queryset_reporter.urls')),
```

Development
-----------

To build the angular client, go to `client` directory and then:

```bash
ng build --prod --watch
```

Permissions
-----------

You should add `queryset_reporter.can_use_reports` to regular users that you want to access the report view/creation page.


Example project credentials
---------------------------

In order to test the project, there's a Example project with a pre defined database that you can use right away.
Here's the credentials:

Admin user:
```
User: admin - Pass: 123
```

Common user:
```
User: tester - Pass: asdfghjklç
```


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

MIT
