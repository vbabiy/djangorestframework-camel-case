#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
import django_rest_framework_camel_case

setup(
    name='django-rest-framework-camel-case',
    version=django_rest_framework_camel_case.__version__,
    description='Camel case JSON support for Django REST framework.',
    long_description=readme + '\n\n' + history,
    author=django_rest_framework_camel_case.__author__,
    author_email=django_rest_framework_camel_case.__email__,
    url=django_rest_framework_camel_case.__url__,
    packages=[
        'django_rest_framework_camel_case',
    ],
    package_dir={'django_rest_framework_camel_case': 'django_rest_framework_camel_case'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django_rest_framework_camel_case',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
