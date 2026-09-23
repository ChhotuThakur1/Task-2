import pytest
from tracker import ExpenseTracker


def test_initial_total_zero():
    tracker = ExpenseTracker()
    assert tracker.total_spent == 0.0


def test_accumulator_addition():
    tracker = ExpenseTracker()
    tracker.add_expense(100.0, "Rent")
    tracker.add_expense(50.0, "Groceries")
    tracker.add_expense(20.0, "Coffee")

    assert tracker.total_spent == 170.0
    assert len(tracker.expenses) == 3


def test_negative_or_zero_expense_raises_value_error():
    tracker = ExpenseTracker()

    with pytest.raises(ValueError):
        tracker.add_expense(0.0)

    with pytest.raises(ValueError):
        tracker.add_expense(-25.50)


def test_category_summary():
    tracker = ExpenseTracker()
    tracker.add_expense(15.0, "Food")
    tracker.add_expense(25.0, "Food")
    tracker.add_expense(10.0, "Travel")

    summary = tracker.get_summary()
    assert summary["Food"] == 40.0
    assert summary["Travel"] == 10.0
