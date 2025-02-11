# test_calculator.py

import pytest
from calculator import Calculator

# Define the fixture
@pytest.fixture
def setup_calculator():
    """Fixture to set up a Calculator instance"""
    return Calculator()

def test_add(setup_calculator):
    """Test addition using fixture"""
    calc = setup_calculator
    assert calc.add(1, 2) == 3

def test_subtract(setup_calculator):
    """Test subtraction using fixture"""
    calc = setup_calculator
    assert calc.subtract(5, 3) == 2

def test_multiply(setup_calculator):
    """Test multiplication using fixture"""
    calc = setup_calculator
    assert calc.multiply(4, 2) == 8

def test_divide(setup_calculator):
    """Test division using fixture"""
    calc = setup_calculator
    assert calc.divide(6, 2) == 3

def test_divide_by_zero(setup_calculator):
    """Test division by zero raises ValueError using fixture"""
    calc = setup_calculator
    with pytest.raises(ValueError):
        calc.divide(6, 0)


