import pathlib
from queryset_reporter import __version__
from setuptools import setup, find_packages


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='queryset_reporter',
    version=__version__,
    url='http://github.com/ricardodani/django-queryset-reporter',
    author='Ricardo Dani',
    author_email='ricardodani@gmail.com',
    description=u'App that creates models of Queryset and generate reports',
    long_description=README,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=['openpyxl'],
    packages=find_packages(),
    python_requires=">3.5",
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
