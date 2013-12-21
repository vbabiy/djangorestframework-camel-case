===============================
Django REST Framework JSON CamelCase
===============================

.. image:: https://badge.fury.io/py/djangorestframework-camel-case.png
    :target: http://badge.fury.io/py/djangorestframework-camel-case
    
.. image:: https://travis-ci.org/vbabiy/djangorestframework-camel-case.png?branch=master
        :target: https://travis-ci.org/vbabiy/djangorestframework-camel-case

.. image:: https://pypip.in/d/djangorestframework-camel-case/badge.png
        :target: https://crate.io/packages/djangorestframework-camel-case?version=latest


Camel case JSON support for Django REST framework.

============
Installation
============

At the command line::

    $ pip djangorestframework-camel-case

Add the render and parser to your django settings file.

    # ...
    REST_FRAMEWORK = {

        'DEFAULT_RENDERER_CLASSES': (
            'djangorestframework_camel_case.CamelCaseJSONRenderer',
            # Any other renders
        ),

        'DEFAULT_PARSER_CLASSES': (
            'djangorestframework_camel_case.CamelCaseJSONRenderer',
            # Any other parsers
        ),
    }
    # ...

* Free software: BSD license
