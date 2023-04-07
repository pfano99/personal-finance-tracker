from datetime import datetime

from flask_login import UserMixin

from finance import db
from finance import login_manager


@login_manager.user_loader
def load_user(_id):
    return User.query.get(_id)


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    accounts = db.relationship('Account', backref='user', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return "User( id: {}, first-name: {}, last-name: {}, email: {})".format(
            self.id, self.first_name, self.last_name, self.email
        )


class Account(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    balance = db.Column(db.Double, nullable=False, default=0.0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    transactions = db.relationship("Transaction", backref="account", lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return "Account( id: {}, name: {}, balance: {})".format(
            self.id, self.name, self.balance,
        )


class Transaction(db.Model):
    __tablename__ = "transaction"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Double, nullable=False, default=0.0)
    transaction_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))
    transaction_type_id = db.Column(db.Integer, db.ForeignKey("transaction_type.id"))

    def __repr__(self) -> str:
        return "Transaction( id: {}, name: {}, amount: {}, date: {}, type: {} )".format(
            self.id, self.name, self.amount, self.transaction_date, self.transaction_type_id
        )


class TransactionType(db.Model):
    __tablename__ = "transaction_type"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self) -> str:
        return "Transaction-Type( id: {}, name: {} )".format(self.id, self.name)
