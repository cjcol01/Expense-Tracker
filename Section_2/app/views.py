from flask import render_template, flash, redirect, url_for, request
from app import app
from .forms import AddExpense, EditExpense, AddGoalForm
from app.models import Expense, Goal
from app import db


@app.route('/home')
def index():
    return render_template('Home.html',
                           title='Homepage',
                        )

@app.route("/visualise")
def visualise():
    total_expense = db.session.query(db.func.sum(Expense.cost)).filter(Expense.expense_type == True).scalar()
    if total_expense is None:
        total_expense = 0

    total_income = db.session.query(db.func.sum(Expense.cost)).filter(Expense.expense_type == False).scalar()
    if total_income is None:
        total_income = 0

    goal = Goal.query.first()  # Query to get the first goal

    print("Debug - goal:", goal)  # Debugging line

    return render_template('Visualise.html', title='Visualise Data', total_expense=total_expense, total_income=total_income, goal=goal)


@app.route('/expenses', methods=['GET'])
def expenses():
    expenses = Expense.query.all()
    return render_template('Expenses.html', expenses=expenses)

@app.route('/add_expense', methods=['GET', 'POST'])
def AddExpensePage():
    form = AddExpense()
    if form.validate_on_submit():
        # Determine the value for expense_type
        expense_type_value = True if form.expense_type.data == "value" else False

        # Create a new Expense object
        new_expense = Expense(
            name=form.name.data,
            cost=form.cost.data,
            expense_type=expense_type_value
        )
        
        # Add the new object to the database session and commit
        db.session.add(new_expense)
        db.session.commit()
        
        flash('Successfully added expense')
        return redirect(url_for('expenses'))

    return render_template('AddExpense.html', form=form)


@app.route('/clear_data', methods=['POST'])
def clear_data():
    try:
        # Delete all records from the Expense table
        num_expense_rows_deleted = db.session.query(Expense).delete()
        
        # Delete all records from the Goal table
        num_goal_rows_deleted = db.session.query(Goal).delete()

        db.session.commit()
        
        flash(f'Successfully deleted {num_expense_rows_deleted} expense records and {num_goal_rows_deleted} goal records.')
    except Exception as e:
        flash('An error occurred while attempting to delete records.')
        db.session.rollback()
    
    return redirect(url_for('expenses'))



@app.route('/edit_expense/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    form = EditExpense()

    if form.validate_on_submit():
        expense.name = form.name.data
        expense.cost = form.cost.data
        db.session.commit()
        flash('Expense updated successfully')
        return redirect(url_for('expenses'))

    return render_template('EditExpense.html', form=form, expense=expense)

# change?
@app.route('/delete_expense/<int:id>', methods=['POST'])
def delete_expense(id):
    try:
        expense_to_delete = Expense.query.get_or_404(id)
        db.session.delete(expense_to_delete)
        db.session.commit()
        return jsonify({'success': True}), 200
    except:
        return jsonify({'success': False}), 500

@app.route('/goal', methods=['GET', 'POST'])
def add_goal():
    
    form = AddGoalForm()
    existing_goal = Goal.query.first()
    
    if request.method == 'GET' and existing_goal:
        # Prepopulate the form fields with existing data
        form.name.data = existing_goal.name
        form.cost.data = existing_goal.cost

    if form.validate_on_submit():
        if existing_goal:
            # Update the existing goal
            existing_goal.name = form.name.data
            existing_goal.cost = form.cost.data
        else:
            # Add a new goal
            new_goal = Goal(name=form.name.data, cost=form.cost.data)
            db.session.add(new_goal)
            
        db.session.commit()
        return redirect(url_for('visualise'))
    
    return render_template('Goal.html', form=form)
