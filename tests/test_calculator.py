from calculator.operations import add, subtract, multiply, divide

def test_addition():
    """Test that the addition function works correctly."""
    assert add(2, 2) == 4
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtraction():
    """Test that the subtraction function works correctly."""
    assert subtract(2, 2) == 0
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1

def test_multiplication():
    """Test that the multiplication function works correctly."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0
    assert multiply(1, -1) == -1

def test_division():
    """Test that the division function works correctly."""
    assert divide(6, 3) == 2
    assert divide(-8, 4) == -2
    assert divide(10, 5) == 2
    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == "Division by zero is not allowed."
