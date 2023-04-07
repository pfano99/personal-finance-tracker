from finance import db
from finance.models import User


def add_user(first_name: str, last_name: str, email: str):
    user = User(first_name=first_name, last_name=last_name, email=email)
    db.session.add(user)
    db.session.commit()
    return


def find_user_by_id(user_id: int) -> User:
    return User.query.get(user_id)


def find_user_by_email(email: str) -> User:
    return User.query.filter_by(email=email).first()
