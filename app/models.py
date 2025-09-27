from datetime import date
from pydantic import BaseModel

class Expense(BaseModel):
    amount: float
    category: str = "Misc"
    note: str | None = None
    date: date

class Budget(BaseModel):
    budget: float
