#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy
from unittest import TestCase

from djangorestframework_camel_case.util import camelize, underscoreize


class UnderscoreToCamelTestCase(TestCase):
    def test_under_to_camel(self):
        data = {
            "title_display": 1
        }
        output = {
            "titleDisplay": 1
        }
        self.assertEqual(camelize(data), output)

    def test_digit_as_part_of_name(self):
        data = {
            "title1_display": 1
        }
        output = {
            "title1Display": 1
        }
        self.assertEqual(camelize(data), output)

    def test_tuples(self):
        data = {
            "multiple_values": (1, 2),
            "data": [1, 3, 4]
        }
        output = {
            "multipleValues": [1, 2],
            "data": [1, 3, 4]
        }
        self.assertEqual(camelize(data), output)

    def test_under_to_camel_input_untouched_for_sequence(self):
        input = [
            {'first_input': 1},
            {'second_input': 2},
        ]
        reference_input = deepcopy(input)
        camelize(input)
        self.assertEqual(input, reference_input)


class CamelToUnderscoreTestCase(TestCase):
    def test_camel_to_under(self):
        data = {
            "titleDisplay": 1
        }
        output = {
            "title_display": 1
        }
        self.assertEqual(underscoreize(data), output)

    def test_digit_as_part_of_name(self):
        data = {
            "title1Display": 1
        }
        output = {
            "title_1_display": 1
        }
        self.assertEqual(underscoreize(data), output)

    def test_camel_to_under_input_untouched_for_sequence(self):
        data = [
            {'firstInput': 1},
            {'secondInput': 2},
        ]
        reference_input = deepcopy(data)
        camelize(data)
        self.assertEqual(data, reference_input)


class CompatibilityTest(TestCase):
    def test_compatibility(self):
        data = {
            "title_245a_display": 1
        }
        self.assertEqual(underscoreize(camelize(data)), data)


class NonStringKeyTest(TestCase):
    def test_non_string_key(self):
        data = {1: "test"}
        self.assertEqual(underscoreize(camelize(data)), data)
