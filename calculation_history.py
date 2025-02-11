# calculation_history.py

from typing import List

class CalculationHistory:
    def __init__(self):
        """Initialize with an empty list of calculations."""
        self.history: List[str] = []

    def add(self, calculation: str) -> None:
        """Add a new calculation to the history."""
        self.history.append(calculation)

    def get_last(self) -> str:
        """Return the last calculation, or 'No history' if empty."""
        if not self.history:
            return 'No history'
        return self.history[-1]
