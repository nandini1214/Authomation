from fastapi import APIRouter, HTTPException
from datetime import date, timedelta
from typing import List
from app.models import Expense, Budget
from app.predictor import predict_budget
import random

router = APIRouter()

# In-memory storage
expenses: List[dict] = []
user_budget: float = 1000  # default budget

# -------------------
# CREATE
# -------------------
@router.post("/expense")
def add_expense(expense: Expense):
    expenses.append(expense)
    return {"message": "Expense added."}

# -------------------
# READ
# -------------------
@router.get("/expenses")
def get_expenses():
    return expenses

@router.get("/expenses/{expense_index}")
def get_expense(expense_index: int):
    try:
        return expenses[expense_index]
    except IndexError:
        raise HTTPException(status_code=404, detail="Expense not found")

# -------------------
# UPDATE
# -------------------
@router.put("/expenses/{expense_index}")
def update_expense(expense_index: int, exp: Expense):
    try:
        expenses[expense_index] = exp.dict()
        return {"message": "Expense updated", "expense": exp}
    except IndexError:
        raise HTTPException(status_code=404, detail="Expense not found")

    
# DELETE

@router.delete("/expenses/{expense_index}")
def delete_expense(expense_index: int):
    try:
        removed = expenses.pop(expense_index)
        return {"message": "Expense deleted", "expense": removed}
    except IndexError:
        raise HTTPException(status_code=404, detail="Expense not found")

# -------------------
# SET/UPDATE BUDGET
# -------------------
@router.post("/budget")
def set_budget(b: Budget):
    global user_budget
    user_budget = b.budget
    return {"message": f"Budget set to {user_budget}"}

# -------------------
# PREDICT BUDGET OVERUSE
# -------------------
@router.get("/budget/predict")
def get_prediction():
    return predict_budget(expenses, user_budget)

@router.get("/summary")
def get_summary():
    if not expenses:
        return {"total": 0, "by_category": {}}
    total = sum(e.amount for e in expenses)
    by_category = {}
    for e in expenses:
        by_category.setdefault(e.category, 0)
        by_category[e.category] += e.amount
    return {"total": total, "by_category": by_category}

@router.get("/prediction")
def prediction():
    return {"prediction": predict_budget(expenses, user_budget)}
