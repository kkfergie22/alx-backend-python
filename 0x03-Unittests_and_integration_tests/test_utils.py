#!/usr/bin/env python3

"""Unit tests for access_nested_map function"""

from utils import memoize
from unittest.mock import patch, MagicMock
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Mapping,
        path: Sequence,
        expected_output: Any
    ) -> None:
        """
        Test that access_nested_map returns the expected output when given a
        nested map and a path to a key or sub-key.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map,
                                         path):
        """
        Test that access_nested_map raises a KeyError with
        the expected error message
        when the given key is not found in the nested map.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    This class contains unit tests for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: dict, mock_get: Mock)\
            -> None:
        """
        Test that the get_json function returns the expected result.

        Args:
        - test_url (str): The URL to pass to get_json.
        - test_payload (dict): The expected response from get_json.
        - mock_get (Mock): A mocked version of requests.get.

        Returns:
        - None
        """
        with patch('requests.get') as mock_get:
            mock_json = Mock(return_value=test_payload)
            mock_get.return_value = Mock(json=mock_json)

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


# class TestMemoize(unittest.TestCase):
#     """
#     This class contains unit tests for the memoize decorator.
#     """

#     def test_memoize(self) -> None:
#         """
#         Test that memoize caches function calls.

#         Returns:
#             None
#         """
#         class TestClass:
#             def a_method(self) -> int:
#                 """
#                 A method that returns 42.

#                 Returns:
#                     int: The integer value 42.
#                 """
#                 return 42

#             @memoize
#             def a_property(self) -> int:
#                 """
#                 A memoized property that calls a_method and returns its result.

#                 Returns:
#                     int: The integer value returned by a_method.
#                 """
#                 return self.a_method()

#         # Mock the a_method function
#         with patch.object(TestClass, 'a_method', return_value=42) as\
#                 mock_a_method:
#             # Create an instance of the TestClass
#             test_obj = TestClass()

#             # Call a_property twice
#             res1 = test_obj.a_property
#             res2 = test_obj.a_property

#             # Assert that the correct result is returned
#             self.assertEqual(res1, 42)
#             self.assertEqual(res2, 42)

#             # Assert that a_method was called only once
#             mock_a_method.assert_called_once()
