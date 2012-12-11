#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-queryset-reporter',
    version='201212111807',
    description='A django admin-site app to persist queryset`s and then make file reports with them.',
    author='Ricardo Dani',
    author_email='ricardod@horizonte.tv.br',
    url='https://github.com/ricardodani/django-queryset-reporter.git',
    packages=['queryset_reporter'],
)
