from finance import app, db, TransactionType

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        transaction_type = [TransactionType(name="SPENT"), TransactionType(name="DEPOSIT")]
        db.session.add_all(transaction_type)
        db.session.commit()
