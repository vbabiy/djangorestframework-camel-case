#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


class CamelToUnderscoreTestCase(TestCase):
    def test_under_to_camel(self):
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
            "title1_display": 1
        }
        self.assertEqual(underscoreize(data), output)


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
