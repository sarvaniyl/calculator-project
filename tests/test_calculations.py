

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

@pytest.fixture
def setup_calculations():
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('15'), Decimal('7'), add))
    Calculations.add_calculation(Calculation(Decimal('30'), Decimal('9'), subtract))

def test_add_calculation(setup_calculations):
    calc = Calculation(Decimal('6'), Decimal('4'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc

def test_get_history(setup_calculations):
    history = Calculations.get_history()
    assert len(history) == 2

def test_clear_history(setup_calculations):
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0

def test_get_latest(setup_calculations):
    latest = Calculations.get_latest()
    assert latest.a == Decimal('30') and latest.b == Decimal('9')

def test_find_by_operation(setup_calculations):
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1

def test_get_latest_with_empty_history():
    Calculations.clear_history()
    assert Calculations.get_latest() is None
