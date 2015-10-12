#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest.case import TestCase

from djangorestframework_camel_case.util import camelize, underscoreize


class UnderscoreToCamelTestCase(TestCase):
    def test_under_to_camel_dict(self):
        input = {
            "title_display": 1
        }
        output = {
            "titleDisplay": 1
        }
        result = camelize(input)
        self.assertEqual(result, output)
        self.assertIsNot(result, input, "should not change original dict")

    def test_under_to_camel_list(self):
        input = [
            {"title_display": 1}
        ]
        output = [
            {"titleDisplay": 1}
        ]
        result = camelize(input)
        self.assertEqual(result, output)
        self.assertIsNot(result, input, "should not change original list")

    def test_under_to_camel_tuple(self):
        input = (
            {"title_display": 1},
        )
        output = (
            {"titleDisplay": 1},
        )
        result = camelize(input)
        self.assertEqual(result, output)
        self.assertIsNot(result, input, "should not change original tuple")

    def test_under_to_camel_nested(self):
        input = {
            "title_display": 1,
            "a_list": [1, "two_three", {"three_four": 5}],
            "a_tuple": ("one_two", 3)
        }
        output = {
            "titleDisplay": 1,
            "aList": [1, "two_three", {"threeFour": 5}],
            "aTuple": ("one_two", 3)
        }
        self.assertEqual(camelize(input), output)


class CamelToUnderscoreTestCase(TestCase):
    def test_camel_to_under_dict(self):
        input = {
            "titleDisplay": 1
        }
        output = {
            "title_display": 1
        }
        result = underscoreize(input)
        self.assertEqual(result, output)
        self.assertIsNot(result, input, "should not change original dict")

    def test_camel_to_under_list(self):
        input = [
            {"titleDisplay": 1}
        ]
        output = [
            {"title_display": 1}
        ]
        result = underscoreize(input)
        self.assertEqual(result, output)
        self.assertIsNot(result, input, "should not change original list")

    def test_camel_to_under_tuple(self):
        input = [
            {"titleDisplay": 1}
        ]
        output = [
            {"title_display": 1}
        ]
        result = underscoreize(input)
        self.assertEqual(result, output)
        self.assertIsNot(result, input, "should not change original tuple")

    def test_camel_to_under_nested(self):
        input = {
            "titleDisplay": 1,
            "aList": [1, "two_three", {"threeFour": 5}],
            "aTuple": ("one_two", 3)
        }
        output = {
            "title_display": 1,
            "a_list": [1, "two_three", {"three_four": 5}],
            "a_tuple": ("one_two", 3)
        }
        self.assertEqual(underscoreize(input), output)


class CompatibilityTest(TestCase):
    def test_compatibility(self):
        input = {
            "title_display": 1,
            "a_list": [1, "two_three", {"three_four": 5}],
            "a_tuple": ("one_two", 3)
        }
        self.assertEqual(underscoreize(camelize(input)), input)
