from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('15'), Decimal('3'), add, Decimal('18')),
    (Decimal('20'), Decimal('8'), subtract, Decimal('12')),
    (Decimal('7'), Decimal('6'), multiply, Decimal('42')),
    (Decimal('50'), Decimal('5'), divide, Decimal('10')),
    (Decimal('8.2'), Decimal('1.3'), add, Decimal('9.5')),
    (Decimal('14.7'), Decimal('2.4'), subtract, Decimal('12.3')),
    (Decimal('5.5'), Decimal('4'), multiply, Decimal('22.0')),
    (Decimal('18'), Decimal('3'), divide, Decimal('6')),
])
def test_calculation_operations(a, b, operation, expected):
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    calc = Calculation(Decimal('12'), Decimal('4'), add)
    expected_repr = "Calculation(12, 4, add)"
    assert calc.__repr__() == expected_repr

def test_divide_by_zero():
    calc = Calculation(Decimal('25'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
