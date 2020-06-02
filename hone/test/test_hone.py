import os
import unittest
import json
from hone import hone
from hone.utils import test_utils

dirname = os.path.dirname(__file__)
csv_A_path = os.path.join(dirname, "data", "small_cats_dataset", "dataset.csv")
json_A_path = os.path.join(dirname, "data", "small_cats_dataset", "nested_dataset.json")
json_schema_A_path = os.path.join(dirname, "data", "small_cats_dataset", "nested_schema.json")
csv_B_path = os.path.join(dirname, "data", "comma_test", "dataset.csv")
json_B_path = os.path.join(dirname, "data", "comma_test", "nested_dataset.json")
csv_C_path = os.path.join(dirname, "data", "quotes_test", "dataset.csv")
json_C_path = os.path.join(dirname, "data", "quotes_test", "nested_dataset.json")

class TestHone(unittest.TestCase):
    def test_nest_small_csv(self):
        h = hone.Hone()
        actual_result = h.convert(csv_A_path)
        expected_result = test_utils.parse_json_file(json_A_path)
        self.assertListEqual(actual_result, expected_result)
    def test_get_schema(self):
        h = hone.Hone()
        actual_result = h.get_schema(csv_A_path)
        expected_result = test_utils.parse_json_file(json_schema_A_path)
        self.assertDictEqual(actual_result, expected_result)
    def test_nest_comma_csv(self):
        h = hone.Hone()
        actual_result = h.convert(csv_B_path)
        expected_result = test_utils.parse_json_file(json_B_path)
        self.assertListEqual(actual_result, expected_result)
    def test_nest_quotes_csv(self):
        h = hone.Hone()
        actual_result = h.convert(csv_C_path)
        expected_result = test_utils.parse_json_file(json_C_path)
        self.assertListEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
