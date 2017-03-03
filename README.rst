===============================
Django REST Framework JSON CamelCase
===============================

.. image:: https://badge.fury.io/py/djangorestframework-camel-case.png
    :target: http://badge.fury.io/py/djangorestframework-camel-case
    
.. image:: https://travis-ci.org/vbabiy/djangorestframework-camel-case.png?branch=master
        :target: https://travis-ci.org/vbabiy/djangorestframework-camel-case

.. image:: https://pypip.in/d/djangorestframework-camel-case/badge.png
        :target: https://img.shields.io/pypi/v/djangorestframework-camel-case.svg


Camel case JSON support for Django REST framework.

============
Installation
============

At the command line::

    $ pip install djangorestframework-camel-case

Add the render and parser to your django settings file.

.. code-block:: python

    # ...
    REST_FRAMEWORK = {

        'DEFAULT_RENDERER_CLASSES': (
            'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
            # Any other renders
        ),

        'DEFAULT_PARSER_CLASSES': (
            'djangorestframework_camel_case.parser.CamelCaseJSONParser',
            # Any other parsers
        ),
    }
    # ...

By default the package uses `rest_framework.renderers.JSONRenderer`. If you want
to use another renderer (the only possible alternative is
`rest_framework.renderers.JSONRenderer`), you must specify it in your django 
settings file.

    # ...
    JSON_CAMEL_CASE = {
        'RENDERER_CLASS': 'rest_framework.renderers.UnicodeJSONRenderer'
    }
    # ...

=============
Running Tests
=============

To run the current test suite, execute the following from the root of he project::

    $ python -m unittest discover

=============
License
=============


* Free software: BSD license
