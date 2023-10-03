from flask import render_template, flash
from app import app
from .forms import AddExpense

@app.route('/')
def index():
    return render_template('Expenses.html',
                           title='Simple template example',
                        )


@app.route('/add', methods=['GET', 'POST'])
def calculator():
    form = AddExpense()
    if form.validate_on_submit():
        flash('Succesfully received form data. %s + %s'%(form.name.data, form.cost.data))
    return render_template('calculator.html',
                           form=form)