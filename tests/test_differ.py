"""
Unit-test various key functions

cd ~/yam_sort
python -m unittest tests.test_differ
or
python -m unittest discover tests

"""

import unittest
from unittest import TestCase

from pathlib import Path
import sys

# This is very messy - if anyone ever finds a better way, let me know. :)
# It's the only way I've found to allow tests to import from directories
# several levels up and over...
TOP_DIR = str(Path(__file__).resolve().parents[1])
sys.path.insert(0, TOP_DIR)

from src.differ import key_diff_something, synchronize_keys

# noinspection PyUnresolvedReferences
from tests.data.some_dicts import set_one, set_two, set_three, set_four, set_five, set_six


class TestGoodSet(TestCase):
    def test_key_diff_ing(self):

        data_set = (set_one, set_two)
        string_set = [('short', 'short_results'), ('long', 'long_results')]

        for cur_data in data_set:
            for string_length, string_val in string_set:
                diff_set = key_diff_something(cur_data['one'], cur_data['two'], format=string_length)

                for test_key, test_val in cur_data[string_val].items():
                    if diff_set[test_key] != test_val:
                        print(f"{diff_set[test_key]} != {test_val}")
                    assert diff_set[test_key] == test_val

    def test_key_sorting(self):

        for one_dataset in [set_three, set_four, set_five]:

            first_data = one_dataset['one']
            second_data = one_dataset['two']

            result_data = synchronize_keys(first_data, second_data)
            diff_set = key_diff_something(first_data, result_data)

            if diff_set['mis_order_keys']:
                print(f"\n\ngot mis_ordered keys:")
                for diff_key, diff_val in diff_set.items():
                    print(f"{diff_key}: {diff_val}")

            assert not diff_set['mis_order_keys']

    def test_missing_key_handling(self):

        first_data = set_six['one']
        second_data = set_six['two']

        result_data = synchronize_keys(first_data, second_data)
        diff_set = key_diff_something(first_data, result_data)

        assert diff_set['missing_keys'] == ['missing-key']

        # Now put the missing key into the second-file, and see what happens
        second_data[diff_set['missing_keys'][0]] = first_data[diff_set['missing_keys'][0]]

        result_data = synchronize_keys(first_data, second_data)
        diff_set = key_diff_something(first_data, result_data)

        assert not diff_set['missing_keys']


if __name__ == '__main__':
    unittest.main()
