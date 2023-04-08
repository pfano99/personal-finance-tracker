from flask import abort

from finance import db
from finance.models import Budget, BudgetItem


def get_budget_by_id(budget_id: int) -> Budget:
    return Budget.query.get(budget_id)


def get_budgets_by_user_id(user_id: int) -> list:
    return Budget.query.filter_by(user_id=user_id)


def get_budgets_by_name_and_user_id(budget_name: str, user_id: int) -> Budget:
    return Budget.query.filter_by(name=budget_name, user_id=user_id).first()


def add_budget(name: str, description: str, user_id: int):
    budget = Budget(
        name=name,
        description=description,
        user_id=user_id
    )
    db.session.add(budget)
    db.session.commit()


def add_budget_item(name: str, price: float, items_count: int, budget_name: str, user_id: int):
    budget = get_budgets_by_name_and_user_id(budget_name, user_id)
    budget_item = BudgetItem(
        name=name,
        price=price,
        budget_id=budget.id,
        items_count=items_count
    )
    db.session.add(budget_item)
    db.session.commit()
