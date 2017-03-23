#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy
from unittest.case import TestCase

from djangorestframework_camel_case.util import camelize, underscoreize


class UnderscoreToCamelTestCase(TestCase):
    def test_under_to_camel(self):
        input = {
            "title_display": 1
        }
        output = {
            "titleDisplay": 1
        }
        self.assertEqual(camelize(input), output)

    def test_under_to_camel_input_untouched_for_sequence(self):
        input = [
            {'first_input': 1},
            {'input_second': 2},
        ]
        reference_input = deepcopy(input)
        camelize(input)
        self.assertEqual(input, reference_input)


class CamelToUnderscoreTestCase(TestCase):
    def test_camel_to_under(self):
        input = {
            "titleDisplay": 1
        }
        output = {
            "title_display": 1
        }
        self.assertEqual(underscoreize(input), output)

    def test_camel_to_under_input_untouched_for_sequence(self):
        input = [
            {'firstInput': 1},
            {'inputSecond': 2},
        ]
        reference_input = deepcopy(input)
        camelize(input)
        self.assertEqual(input, reference_input)


class CompatibilityTest(TestCase):
    def test_compatibility(self):
        input = {
            "title_245a_display": 1
        }
        self.assertEqual(underscoreize(camelize(input)), input)
