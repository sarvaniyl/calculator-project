# test_calculation_history.py

import pytest
from calculation_history import CalculationHistory

# Define the fixture
@pytest.fixture
def setup_history():
    """Fixture to set up a CalculationHistory instance"""
    return CalculationHistory()

def test_add_calculation(setup_history):
    """Test adding a calculation to history using fixture"""
    history = setup_history
    history.add("1 + 1 = 2")
    assert history.history == ["1 + 1 = 2"]

def test_get_last_calculation(setup_history):
    """Test getting the last calculation using fixture"""
    history = setup_history
    history.add("1 + 1 = 2")
    history.add("2 + 2 = 4")
    assert history.get_last() == "2 + 2 = 4"

def test_get_last_empty_history(setup_history):
    """Test getting the last calculation from an empty history using fixture"""
    history = setup_history
    assert history.get_last() == "No history"


