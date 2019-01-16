====================================
Django REST Framework JSON CamelCase
====================================

.. image:: https://travis-ci.org/vbabiy/djangorestframework-camel-case.png?branch=master
        :target: https://travis-ci.org/vbabiy/djangorestframework-camel-case

.. image:: https://badge.fury.io/py/djangorestframework-camel-case.svg
    :target: https://badge.fury.io/py/djangorestframework-camel-case

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
            'django_rest_framework_camel_case.render.CamelCaseJSONRenderer',
            # Any other renders
        ),

        'DEFAULT_PARSER_CLASSES': (
            'django_rest_framework_camel_case.parser.CamelCaseJSONParser',
            # Any other parsers
        ),
    }
    # ...

=================
Swapping Renderer and Parser
=================

By default the package uses `rest_framework.renderers.JSONRenderer` and `rest_framework.parsers.JSONParser`. 
If you want to use another renderer or parser, you must specify it in your django settings file.

Currently Support

.. code-block:: python

    'RENDERER_CLASS': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.UnicodeJSONRenderer', # only available in DRF < 3.0
        'rest_framework_google_json_style_api.renderers.JSONRenderer',
        'rest_framework_json_api.renderers.JSONRenderer',
    ),
    'PARSER_CLASS': (
        'rest_framework.parsers.JSONParser',
        'rest_framework_google_json_style_api.parsers.JSONParser',
        'rest_framework_json_api.parsers.JSONParser',
    )


Specify it in your django settings file.

.. code-block:: python

    # ...
    JSON_CAMEL_CASE = {
        'RENDERER_CLASS': 'rest_framework_google_json_style_api.renderers.JSONRenderer',
        'PARSER_CLASS': 'rest_framework_google_json_style_api.parsers.JSONParser',
    }
    # ...

=====================
Underscoreize Options
=====================

As raised in https://github.com/krasa/StringManipulation/issues/8#issuecomment-121203018
there are two conventions of snake case.

.. code-block:: none

    # Case 1 (Package default)
    v2Counter -> v_2_counter
    fooBar2 -> foo_bar_2

    # Case 2
    v2Counter -> v2_counter
    fooBar2 -> foo_bar2


By default, the package uses the first case. To use the second case, specify it in your django settings file.

.. code-block:: python

    REST_FRAMEWORK = {
        # ...
        'JSON_UNDERSCOREIZE': {
            'no_underscore_before_number': True,
        },
        # ...
    }




=============
Running Tests
=============

To run the current test suite, execute the following from the root of he project::

    $ python -m unittest discover


=======
License
=======

* Free software: BSD license
