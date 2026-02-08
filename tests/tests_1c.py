"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_positives():
    assert max_subarray_sum([1, 2, 3, 4, 5, 6]) == 21          # Test for positive numbers
    assert max_subarray_sum([4, 6, 3, 2, 1, 6]) == 22          # Test for positive numbers

def test_negatives():
    assert max_subarray_sum([-1, -7, -4, -5]) == -1            # Test for negative numbers
    assert max_subarray_sum([-6, -13, -4, -5, -5]) == -4       # Test for negative numbers

def test_all():
    assert max_subarray_sum([6, -6, 7, 4, -5]) == 11           # Test for all numbers
    assert max_subarray_sum([2, 3, -1]) == 5                   # Test for all numbers

def test_empty():
    with pytest.raises(IndexError, match="Array cannot be empty."):
        max_subarray_sum([])               # Test response to an empty array

if __name__ == "__main__":
    pytest.main()