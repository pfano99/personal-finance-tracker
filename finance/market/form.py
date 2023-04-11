from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired


class StockForm(FlaskForm):
    ticker = StringField('Ticker/Symbol', validators=[DataRequired()])
    bought_at = DecimalField('Bought at', validators=[DataRequired()])
    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')
