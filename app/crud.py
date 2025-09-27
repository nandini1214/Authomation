from sqlalchemy.orm import Session
from app.db import ExpenseDB, BudgetDB
from app.models import Expense, Budget
from datetime import date

# Add Expense
def create_expense(db: Session, exp: Expense):
    db_exp = ExpenseDB(**exp.dict())
    db.add(db_exp)
    db.commit()
    db.refresh(db_exp)
    return db_exp

# List Expenses
def get_expenses(db: Session):
    return db.query(ExpenseDB).all()

# Update Expense
def update_expense(db: Session, expense_id: int, exp: Expense):
    db_exp = db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()
    if not db_exp:
        return None
    for key, value in exp.dict().items():
        setattr(db_exp, key, value)
    db.commit()
    db.refresh(db_exp)
    return db_exp

# Delete Expense
def delete_expense(db: Session, expense_id: int):
    db_exp = db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()
    if not db_exp:
        return None
    db.delete(db_exp)
    db.commit()
    return db_exp

# Budget CRUD
def set_budget(db: Session, budget: Budget):
    db_budget = db.query(BudgetDB).first()
    if db_budget:
        db_budget.budget = budget.budget
    else:
        db_budget = BudgetDB(budget=budget.budget)
        db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

def get_budget(db: Session):
    return db.query(BudgetDB).first()
