from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, SelectField
from wtforms.validators import DataRequired

from finance.budget.service import get_budgets_by_user_id


class BudgetForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description/Goal')
    submit = SubmitField('Submit')


class BudgetItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    item_count = IntegerField('Quantity', validators=[DataRequired()], default=1)
    budget = SelectField("Budget", validators=[DataRequired()],
                         choices=lambda: [i.name for i in get_budgets_by_user_id(current_user.id)])
    submit = SubmitField('Add Item')
