from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

from finance.account.form import AccountForm
from finance.account.service import add_account, get_accounts_by_user_id, get_account_by_id
from finance.transaction.forms import TransactionForm
from finance.transaction.service import add_transaction

main = Blueprint('Main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/dashboard', methods=['GET', 'POST'])
@main.route('/dashboard/<int:account_id>', methods=['GET', 'POST'])
@login_required
def dashboard(account_id: int = -1):
    transaction_form = TransactionForm()
    account_form = AccountForm()

    if request.method == 'POST':
        is_form_valid = False
        if transaction_form.validate_on_submit():
            is_form_valid = True
            add_transaction(name=transaction_form.name.data,
                            transaction_date=transaction_form.transaction_date.data,
                            amount=transaction_form.amount.data, account_name=transaction_form.account.data,
                            transaction_type=transaction_form.transaction_type.data)
            flash("Transaction successfully added", "success")

        if account_form.validate_on_submit():
            is_form_valid = True
            add_account(name=account_form.name.data, balance=account_form.balance.data)
            flash("Account successfully added", "success")

        if not is_form_valid:
            flash("Failed to validate form input", "danger")

    accounts = get_accounts_by_user_id(current_user.id)
    if account_id != -1:
        current_account = get_account_by_id(account_id)
    else:
        current_account = accounts[0]

    context = {
        "_account_form": account_form,
        "_transaction_form": transaction_form,
        "accounts": accounts,
        "current_account": current_account
    }

    return render_template('dashboard.html', context=context)
