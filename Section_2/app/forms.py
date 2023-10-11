from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, StringField, RadioField
from wtforms.validators import DataRequired

class AddExpense(FlaskForm):
    name = StringField("name", validators=[DataRequired()], render_kw={"placeholder": "Name"})
    cost = DecimalField("cost", places=2, rounding=None, render_kw={"placeholder": "Expense cost"})
    expense_type = RadioField("type", validators=[DataRequired()], choices=[("value","Expense"),("value2","Income")], default="value")

class EditExpense(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    cost = DecimalField('Cost', validators=[DataRequired()])

class AddGoalForm(FlaskForm):
    name = StringField("name", render_kw={"placeholder": "Goal Name"})
    cost = DecimalField("cost", places=2, rounding=None, render_kw={"placeholder": "Goal Value"})
