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
    """Test case class for access_nested_map function"""

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
        """Test for access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access_nested_map raises a KeyError
        when the given key is not found in the nested map.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_error_message)


class TestGetJson(unittest.TestCase):
    @patch('requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_json = Mock(return_value=test_payload)
        mock_get.return_value = Mock(json=mock_json)

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    This class contains unit tests for the memoize decorator.
    """

    def test_memoize(self):
        """
        Test that memoize caches function calls.
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Mock the a_method function
        with patch.object(TestClass, 'a_method', return_value=42) as\
                mock_a_method:
            test_obj = TestClass()
            # Call a_property twice
            res1 = test_obj.a_property
            res2 = test_obj.a_property
            # Assert that the correct result is returned
            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)
            # Assert that a_method was called only once
            mock_a_method.assert_called_once()
