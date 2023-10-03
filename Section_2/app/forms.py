from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, StringField
from wtforms.validators import DataRequired

class CalculatorForm(FlaskForm):
    number1 = IntegerField("number", validators=[DataRequired()])
    number2 = IntegerField("number2", validators=[DataRequired()])

class AddExpense(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    cost = DecimalField("cost", places=2, rounding=None)