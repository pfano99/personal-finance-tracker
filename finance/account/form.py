from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired


class AccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    balance = DecimalField('Balance', validators=[DataRequired()], rounding=2)
    submit = SubmitField('Submit')
