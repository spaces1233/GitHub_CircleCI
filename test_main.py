import pytest
from main import add_numbers

def test_add_numbers():
    assert add_numbers(3, 3) == 5
    
    assert add_numbers(-1, 1) == 0

def test_add_large_numbers():
    assert add_numbers(10**6, 2 * 10**6) == 3000000
    
    assert add_numbers(10**6, 10**6) == 2000000

def test_add_floating_point_numbers():
    assert add_numbers(2.5, 3.5) == 6.0
    
    assert add_numbers(1.5, 2.5) == 4.0
