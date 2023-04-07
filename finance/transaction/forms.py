from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, DateField, SubmitField
from wtforms.validators import DataRequired

from finance.models import Account
from finance.account.service import get_accounts_by_user_id
from finance.transaction.service import get_all_transaction_types


def generate_account_names() -> list:
    account = get_accounts_by_user_id(current_user.id)
    return [i for i in map(map_account_names, account)]


def map_account_names(account: Account) -> str:
    return account.name


def map_transaction_type_names() -> list:
    transaction_types = get_all_transaction_types()
    return [i for i in map(lambda x: x.name, transaction_types)]


class TransactionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    transaction_date = DateField('Transaction Date', validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired()], rounding=2)
    account = SelectField('Account', choices=lambda: generate_account_names())
    transaction_type = SelectField('Transaction Type', choices=lambda: map_transaction_type_names())
    submit = SubmitField('Submit')
