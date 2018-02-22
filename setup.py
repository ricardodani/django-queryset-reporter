#!/usr/bin/env python
#-*- coding: utf-8 -*-

from queryset_reporter import __version__
from distutils.core import setup
from setuptools import find_packages

setup(
    name='queryset_reporter',
    version=__version__,
    url='http://github.com/ricardodani/django-queryset-reporter',
    author='Ricardo Dani',
    author_email='ricardod@horizonte.tv.br',
    description=u'App to generate Querysets and Reports based on them.',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django >=1.3, <1.5',
        'south',
        'openpyxl',
        'django-grappelli >=2.3.8, <=2.4.10',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
)
