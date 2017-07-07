#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy
from unittest import TestCase

from djangorestframework_camel_case.util import camelize, underscoreize


class UnderscoreToCamelTestCase(TestCase):
    def test_under_to_camel_keys(self):
        data = {
            "two_word": 1,
            "long_key_with_many_underscores": 2,
            "only_1_key": 3,
            "only_one_letter_a": 4,
            "b_only_one_letter": 5,
            "only_c_letter": 6,
            "mix_123123a_and_letters": 7,
        }
        output = {
            "twoWord": 1,
            "longKeyWithManyUnderscores": 2,
            "only1Key": 3,
            "onlyOneLetterA": 4,
            "bOnlyOneLetter": 5,
            "onlyCLetter": 6,
            "mix123123aAndLetters": 7
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

    def test_camel_to_under_input_untouched_for_sequence(self):
        data = [
            {'firstInput': 1},
            {'secondInput': 2},
        ]
        reference_input = deepcopy(data)
        camelize(data)
        self.assertEqual(data, reference_input)


class CamelToUnderscoreTestCase(TestCase):
    def test_camel_to_under_keys(self):
        data = {
            "twoWord": 1,
            "longKeyWithManyUnderscores": 2,
            "only1Key": 3,
            "onlyOneLetterA": 4,
            "bOnlyOneLetter": 5,
            "onlyCLetter": 6,
            "mix123123aAndLetters":7
        }
        output = {
            "two_word": 1,
            "long_key_with_many_underscores": 2,
            "only_1_key": 3,
            "only_one_letter_a": 4,
            "b_only_one_letter": 5,
            "only_c_letter": 6,
            "mix_123123a_and_letters": 7
        }
        self.assertEqual(underscoreize(data), output)

    def test_under_to_camel_input_untouched_for_sequence(self):
        data = [
            {'first_input': 1},
            {'second_input': 2},
        ]
        reference_input = deepcopy(data)
        underscoreize(data)
        self.assertEqual(data, reference_input)


class NonStringKeyTest(TestCase):
    def test_non_string_key(self):
        data = {1: "test"}
        self.assertEqual(underscoreize(camelize(data)), data)
