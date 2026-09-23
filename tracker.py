from dataclasses import dataclass
from typing import List


@dataclass
class Expense:
    category: str
    amount: float


class ExpenseTracker:
    def __init__(self):
        self.expenses: List[Expense] = []
        self._total_spent: float = 0.0

    @property
    def total_spent(self) -> float:
        return self._total_spent

    def add_expense(self, amount: float, category: str = "General") -> None:
        """
        Validates the input and applies the accumulator pattern:
        total = total + new_expense
        """
        if amount <= 0:
            raise ValueError("Expense amount must be greater than zero.")

        self.expenses.append(Expense(category=category.strip(), amount=amount))
        self._total_spent += amount

    def get_summary(self) -> dict:
        """Returns total spending grouped by category."""
        category_totals = {}
        for item in self.expenses:
            category_totals[item.category] = (
                category_totals.get(item.category, 0.0) + item.amount
            )
        return category_totals
