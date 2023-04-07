from flask_login import current_user

from finance import db
from finance.models import Account


def get_account_by_id(account_id: int) -> Account:
    return Account.query.get(account_id)


def get_accounts_by_user_id(user_id: int) -> list:
    return Account.query.filter_by(user_id=user_id)


def get_accounts_by_name_and_user_id(name: str, user_id) -> Account:
    return Account.query.filter_by(user_id=user_id, name=name).first()


def add_account(name: str, balance: float):
    account = Account(name=name, balance=balance, user_id=current_user.id)
    db.session.add(account)
    db.session.commit()


def update_account(account_id: int, name: str, balance: float):
    account = get_account_by_id(account_id)
    account.name = name
    account.balance = balance
    db.session.commit()


def delete_account(account_id: int):
    account = get_account_by_id(account_id)
    db.session.delete(account)
    db.session.commit()
