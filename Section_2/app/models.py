from app import db

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    cost = db.Column(db.Float)
    expense_type = db.Column(db.Boolean, default=False)

# class Income(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200))
#     cost = db.Column(db.Float)
#     # expense_type = db.Column(db.String(7))

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    cost = db.Column(db.Float)