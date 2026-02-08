"""
tests_1c.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_positives():
    assert two_sum([1, 2, 3, 4, 5, 6] , 3) == [0, 1]          # Test for positive numbers
    assert two_sum([4, 6, 3, 2, 1, 6], 4) == [2, 4]           # Test for positive numbers

def test_negatives():
    assert two_sum([-1, -7, -4, -5], -5) == [0, 2]            # Test for negative numbers
    assert two_sum([-6, -13, -4, -5, -5], -9) == [2, 3]       # Test for negative numbers

def test_all():
    assert two_sum([6, -6, 7, 4, -5], 0) == [0, 1]            # Test for all numbers
    assert two_sum([2, 3, -1], 2) == [1, 2]          # Test for all numbers

if __name__ == "__main__":
    pytest.main()