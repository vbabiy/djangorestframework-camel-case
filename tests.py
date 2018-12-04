#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import deepcopy
from unittest import TestCase

from django.http.request import MultiValueDict

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
            "no_underscore_before123": 8
        }
        output = {
            "twoWord": 1,
            "longKeyWithManyUnderscores": 2,
            "only1Key": 3,
            "onlyOneLetterA": 4,
            "bOnlyOneLetter": 5,
            "onlyCLetter": 6,
            "mix123123aAndLetters": 7,
            "noUnderscoreBefore123": 8
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
            "mix123123aAndLetters": 7,
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

    def test_camel_to_under_keys_with_no_underscore_before_number(self):
        data = {'noUnderscoreBefore123': 1}
        output = {'no_underscore_before123': 1}
        options = {'no_underscore_before_number': True}
        self.assertEqual(underscoreize(data, **options), output)

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


class GeneratorAsInputTestCase(TestCase):
    def _underscore_generator(self):
        yield {'simple_is_better': 'than complex'}
        yield {'that_is': 'correct'}

    def _camel_generator(self):
        yield {'simpleIsBetter': 'than complex'}
        yield {'thatIs': 'correct'}

    def test_camelize_iterates_over_generator(self):
        data = self._underscore_generator()
        output = [
            {'simpleIsBetter': 'than complex'},
            {'thatIs': 'correct'},
        ]
        self.assertEqual(camelize(data), output)

    def test_underscoreize_iterates_over_generator(self):
        data = self._camel_generator()
        output = [
            {'simple_is_better': 'than complex'},
            {'that_is': 'correct'},
        ]
        self.assertEqual(underscoreize(data), output)


class MultiValueDictTestCase(TestCase):
    def test_underscoreize_and_saving_all_values(self):
        data = MultiValueDict([])
        data.setlist('testGetParameter', ['value1', 'value2'])
        expected_value_list = ['value1', 'value2']
        self.assertIsInstance(data, MultiValueDict)
        self.assertEqual(underscoreize(data).getlist('test_get_parameter'), expected_value_list)
