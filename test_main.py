import pytest
from main import add_numbers

def test_add_numbers():
    # This test will pass
    assert add_numbers(2, 3) == 5  # Pass: 2 + 3 = 5
    
    # This test will fail: expected result is incorrect
    assert add_numbers(-1, 1) == 1  # Fail: It should be 0, but we expect 1

def test_add_large_numbers():
    # This test will pass
    assert add_numbers(10**6, 10**6) == 2000000  # Pass: 10^6 + 10^6 = 2000000
    
    # This test will fail: expected result is incorrect
    assert add_numbers(10**6, 10**6) == 1500000  # Fail: It should be 2000000, but we expect 1500000

def test_add_floating_point_numbers():
    # This test will pass
    assert add_numbers(2.5, 3.5) == 6.0  # Pass: 2.5 + 3.5 = 6.0
    
    # This test will fail: expected result is incorrect
    assert add_numbers(0.1, 0.2) == 0.4  # Fail: It should be 0.3, but we expect 0.4
