# main.py

from calculator import Calculator
from calculation_history import CalculationHistory

def main():
    calc_history = CalculationHistory()

    # Example operations
    result_add = Calculator.add(3, 5)
    calc_history.add(f"3 + 5 = {result_add}")

    result_subtract = Calculator.subtract(10, 4)
    calc_history.add(f"10 - 4 = {result_subtract}")

    result_multiply = Calculator.multiply(4, 6)
    calc_history.add(f"4 * 6 = {result_multiply}")

    try:
        result_divide = Calculator.divide(10, 0)  # This will raise an exception
        calc_history.add(f"10 / 0 = {result_divide}")
    except ValueError as e:
        calc_history.add(f"10 / 0 = Error: {str(e)}")

    # Print the calculation history
    print("Calculation History:")
    for entry in calc_history.history:
        print(entry)

if __name__ == "__main__":
    main()
