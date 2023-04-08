from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

from finance.budget.forms import BudgetForm, BudgetItemForm
from finance.budget.service import get_budget_by_id, get_budgets_by_user_id, add_budget, add_budget_item

budget = Blueprint("Budget", __name__)


@budget.route("/")
@budget.route("/<int:budget_id>")
def get_budget(budget_id: int = -1):
    if budget_id != -1:
        current_budget = get_budget_by_id(budget_id)
    else:
        budgets = get_budgets_by_user_id(current_user.id)
        current_budget = budgets[0] if budgets.count() > 0 else None

    budget_form = BudgetForm()
    budget_item_form = BudgetItemForm()
    context = {
        "_budget_form": budget_form,
        "_budget_item_form": budget_item_form,
        "current_budget": current_budget
    }
    return render_template("budget/budget.html", context=context)


@budget.route("/add", methods=['POST'])
def post_add_budget():
    form = BudgetForm()
    if form.validate_on_submit():
        add_budget(name=form.name.data, description=form.description.data, user_id=current_user.id)
    return redirect(url_for("Budget.get_budget"))


@budget.route("/item/add", methods=['POST'])
def post_add_budget_item():
    form = BudgetItemForm()
    if form.validate_on_submit():
        add_budget_item(name=form.name.data, price=form.price.data, items_count=form.item_count.data,
                        budget_name=form.budget.data, user_id=current_user.id)

    return redirect(url_for("Budget.get_budget"))


@budget.route("/update", methods=['PUT'])
def put_update_budget():
    pass
