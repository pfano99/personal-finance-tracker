from datetime import datetime

from flask_login import current_user

from finance import db
from finance.account.service import get_accounts_by_name_and_user_id
from finance.models import Transaction, TransactionType


def get_transaction_by_id(_id: int) -> Transaction:
    return Transaction.query.get(_id)


def get_transactions_by_user_id(user_id: int) -> list:
    return Transaction.query.filter_by(user_id)


def add_transaction(name: str, transaction_date: datetime, amount: float, transaction_type: str, account_name: str):
    tt = get_transaction_type_by_name(transaction_type)
    account = get_accounts_by_name_and_user_id(account_name, current_user.id)
    transaction = Transaction(
        name=name, amount=amount, transaction_date=transaction_date, transaction_type_id=tt.id, account_id=account.id
    )
    db.session.add(transaction)
    db.session.commit()


def get_all_transaction_types() -> list:
    return TransactionType.query.all()


def get_transaction_type_by_name(name: str) -> TransactionType:
    return TransactionType.query.filter_by(name=name).first()
