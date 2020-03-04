from copy import deepcopy
from unittest import TestCase

from django.conf import settings
from django.http import QueryDict
from django.utils.functional import lazy

from rest_framework.utils.serializer_helpers import ReturnDict

from djangorestframework_camel_case.util import camelize, underscoreize

settings.configure()


class ImportTest(TestCase):
    def test_import_all(self):
        """
        A quick test that just imports everything, should crash in case any Django or DRF modules change
        """
        from djangorestframework_camel_case import parser
        from djangorestframework_camel_case import render
        from djangorestframework_camel_case import settings

        assert parser
        assert render
        assert settings


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
            "mix_123123aa_and_letters_complex": 8,
            "no_underscore_before123": 9,
        }
        output = {
            "twoWord": 1,
            "longKeyWithManyUnderscores": 2,
            "only1Key": 3,
            "onlyOneLetterA": 4,
            "bOnlyOneLetter": 5,
            "onlyCLetter": 6,
            "mix123123aAndLetters": 7,
            "mix123123aaAndLettersComplex": 8,
            "noUnderscoreBefore123": 9,
        }
        self.assertEqual(camelize(data), output)

    def test_tuples(self):
        data = {"multiple_values": (1, 2), "data": [1, 3, 4]}
        output = {"multipleValues": [1, 2], "data": [1, 3, 4]}
        self.assertEqual(camelize(data), output)

    def test_camel_to_under_input_untouched_for_sequence(self):
        data = [{"firstInput": 1}, {"secondInput": 2}]
        reference_input = deepcopy(data)
        camelize(data)
        self.assertEqual(data, reference_input)

    def test_recursive_with_ignored_keys(self):
        ignore_fields = ("ignore_me", "newKey")
        data = {
            "ignore_me": {"no_change_recursive": 1},
            "change_me": {"change_recursive": 2},
            "new_key": {"also_no_change": 3},
        }
        output = {
            "ignoreMe": {"no_change_recursive": 1},
            "changeMe": {"changeRecursive": 2},
            "newKey": {"also_no_change": 3},
        }
        self.assertEqual(camelize(data, ignore_fields=ignore_fields), output)


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
            "mix123123aaAndLettersComplex": 8,
            "wordWITHCaps": 9,
            "key10": 10,
            "anotherKey1": 11,
            "anotherKey10": 12,
            "optionS1": 13,
            "optionS10": 14,
        }
        output = {
            "two_word": 1,
            "long_key_with_many_underscores": 2,
            "only_1_key": 3,
            "only_one_letter_a": 4,
            "b_only_one_letter": 5,
            "only_c_letter": 6,
            "mix_123123a_and_letters": 7,
            "mix_123123aa_and_letters_complex": 8,
            "word_with_caps": 9,
            "key_10": 10,
            "another_key_1": 11,
            "another_key_10": 12,
            "option_s_1": 13,
            "option_s_10": 14,
        }
        self.assertEqual(underscoreize(data), output)

    def test_camel_to_under_keys_with_no_underscore_before_number(self):
        data = {"noUnderscoreBefore123": 1}
        output = {"no_underscore_before123": 1}
        options = {"no_underscore_before_number": True}
        self.assertEqual(underscoreize(data, **options), output)

    def test_under_to_camel_input_untouched_for_sequence(self):
        data = [{"first_input": 1}, {"second_input": 2}]
        reference_input = deepcopy(data)
        underscoreize(data)
        self.assertEqual(data, reference_input)

    def test_recursive_with_ignored_keys(self):
        ignore_fields = ("ignore_me", "newKey")
        data = {
            "ignoreMe": {"noChangeRecursive": 1},
            "changeMe": {"changeRecursive": 2},
            "newKey": {"alsoNoChange": 3},
        }
        output = {
            "ignore_me": {"noChangeRecursive": 1},
            "change_me": {"change_recursive": 2},
            "new_key": {"alsoNoChange": 3},
        }
        self.assertEqual(underscoreize(data, ignore_fields=ignore_fields), output)


class NonStringKeyTest(TestCase):
    def test_non_string_key(self):
        data = {1: "test"}
        self.assertEqual(underscoreize(camelize(data)), data)


def return_string(text):
    return text


lazy_func = lazy(return_string, str)


class PromiseStringTest(TestCase):
    def test_promise_strings(self):
        data = {lazy_func("test_key"): lazy_func("test_value value")}
        camelized = camelize(data)
        self.assertEqual(camelized, {"testKey": "test_value value"})
        result = underscoreize(camelized)
        self.assertEqual(result, {"test_key": "test_value value"})


class ReturnDictTest(TestCase):
    def test_return_dict(self):
        data = ReturnDict({"id": 3, "value": "val"}, serializer=object())
        camelized = camelize(data)
        self.assertEqual(data, camelized)
        self.assertEqual(data.serializer, camelized.serializer)


class GeneratorAsInputTestCase(TestCase):
    def _underscore_generator(self):
        yield {"simple_is_better": "than complex"}
        yield {"that_is": "correct"}

    def _camel_generator(self):
        yield {"simpleIsBetter": "than complex"}
        yield {"thatIs": "correct"}

    def test_camelize_iterates_over_generator(self):
        data = self._underscore_generator()
        output = [{"simpleIsBetter": "than complex"}, {"thatIs": "correct"}]
        self.assertEqual(camelize(data), output)

    def test_underscoreize_iterates_over_generator(self):
        data = self._camel_generator()
        output = [{"simple_is_better": "than complex"}, {"that_is": "correct"}]
        self.assertEqual(underscoreize(data), output)


class CamelToUnderscoreQueryDictTestCase(TestCase):
    def test_camel_to_under_keys(self):
        query_dict = QueryDict("testList=1&testList=2", mutable=True)
        data = {
            "twoWord": 1,
            "longKeyWithManyUnderscores": 2,
            "only1Key": 3,
            "onlyOneLetterA": 4,
            "bOnlyOneLetter": 5,
            "onlyCLetter": 6,
            "mix123123aAndLetters": 7,
            "mix123123aaAndLettersComplex": 8,
            "wordWITHCaps": 9,
            "key10": 10,
            "anotherKey1": 11,
            "anotherKey10": 12,
            "optionS1": 13,
            "optionS10": 14,
        }
        query_dict.update(data)

        output_query = QueryDict("test_list=1&test_list=2", mutable=True)

        output = {
            "two_word": 1,
            "long_key_with_many_underscores": 2,
            "only_1_key": 3,
            "only_one_letter_a": 4,
            "b_only_one_letter": 5,
            "only_c_letter": 6,
            "mix_123123a_and_letters": 7,
            "mix_123123aa_and_letters_complex": 8,
            "word_with_caps": 9,
            "key_10": 10,
            "another_key_1": 11,
            "another_key_10": 12,
            "option_s_1": 13,
            "option_s_10": 14,
        }
        output_query.update(output)
        self.assertEqual(underscoreize(query_dict), output_query)
