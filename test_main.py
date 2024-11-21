import pytest
from main import add_numbers

def test_add_numbers():
    # This test will pass
    assert add_numbers(2, 3) == 5  # Pass: 2 + 3 = 5
    
    # This test will fail: expected result is incorrect
    assert add_numbers(-1, 1) == 1  # Fail: Result will be 0, but we expect 1

def test_add_large_numbers():
    # This test will fail: expected result is incorrect
    assert add_numbers(10**6, 2 * 10**6) == 2000000  # Fail: 10^6 + 2 * 10^6 = 3000000, not 2000000
    
    # This test will fail: expected result is incorrect
    assert add_numbers(10**6, 10**6) == 1500000  # Fail: 10^6 + 10^6 = 2000000, not 1500000

def test_add_floating_point_numbers():
    # This test will pass
    assert add_numbers(2.5, 3.5) == 6.0  # Pass: 2.5 + 3.5 = 6.0
    
    # Second assertion: This will pass
    assert add_numbers(1.1, 2.2) == 3.3  # Pass: 1.1 + 2.2 = 3.3 exactly
