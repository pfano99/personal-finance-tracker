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
    budgets = db.relationship('Budget', backref='user', lazy=True, cascade="all, delete-orphan")

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


class Budget(db.Model):
    __tablename__ = "budget"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    budget_items = db.relationship("BudgetItem", lazy=True, backref="budget", cascade="all, delete-orphan")

    def __repr__(self):
        return "Budget ( id: {}, name: {} )".format(self.id, self.name)

    @property
    def total_cost(self) -> int:
        res = 0
        for item in self.budget_items:
            res += item.price * item.items_count
        return res


class BudgetItem(db.Model):
    __tablename__ = "budget_item"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Double, nullable=False)
    items_count = db.Column(db.Integer, nullable=False, default=1)  # rename to quantity
    budget_id = db.Column(db.Integer, db.ForeignKey("budget.id"))

    def __repr__(self):
        return "BudgetItem ( id: {}, name: {}, price: {}, item-count: {} )".format(
            self.id, self.name, self.price, self.items_count)


class Stock(db.Model):
    __tablename__ = "stock"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(15), nullable=False)
    bought_at = db.Column(db.Double, nullable=False)
    amount = db.Column(db.Double, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return "Sock( id: {}, ticker: {}, bought_at: {}, amount: {}".format(
            self.id, self.ticker, self.bought_at, self.amount
        )
