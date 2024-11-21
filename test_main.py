import pytest
from main import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_add_large_numbers():
    assert add_numbers(10**6, 10**6) == 2000000  # Test with large numbers

def test_add_floating_point_numbers():
    assert add_numbers(2.5, 3.5) == 6.0  # Test with floating point numbers
