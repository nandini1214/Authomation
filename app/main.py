from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal, ExpenseDB, BudgetDB
from app.models import Expense, Budget
from app.predictor import predict_budget

app = FastAPI(title="SmartBudget Hackathon")
origins = [
    "http://localhost:5173",  # your Vite dev server
    "http://127.0.0.1:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # allow only specific origins
    allow_credentials=True,
    allow_methods=["*"],         # allow GET, POST, PUT, DELETE
    allow_headers=["*"],         # allow headers
)
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD Endpoints
@app.post("/expenses")
def add_expense(exp: Expense, db: Session = Depends(get_db)):
    db_exp = ExpenseDB(**exp.dict())
    db.add(db_exp)
    db.commit()
    db.refresh(db_exp)
    return db_exp

@app.get("/expenses")
def list_expenses(db: Session = Depends(get_db)):
    return db.query(ExpenseDB).all()

@app.put("/expenses/{expense_id}")
def edit_expense(expense_id: int, exp: Expense, db: Session = Depends(get_db)):
    db_exp = db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()
    if not db_exp:
        raise HTTPException(status_code=404, detail="Expense not found")
    for key, value in exp.dict().items():
        setattr(db_exp, key, value)
    db.commit()
    db.refresh(db_exp)
    return db_exp

@app.delete("/expenses/{expense_id}")
def remove_expense(expense_id: int, db: Session = Depends(get_db)):
    db_exp = db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()
    if not db_exp:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(db_exp)
    db.commit()
    return {"message": "Deleted successfully"}

@app.post("/budget")
def update_budget(b: Budget, db: Session = Depends(get_db)):
    db_budget = db.query(BudgetDB).first()
    if db_budget:
        db_budget.budget = b.budget
    else:
        db_budget = BudgetDB(budget=b.budget)
        db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

@app.get("/budget/predict")
def predict(db: Session = Depends(get_db)):
    expenses = db.query(ExpenseDB).all()
    budget = db.query(BudgetDB).first()
    user_budget = budget.budget if budget else 1000
    return predict_budget([{
        "amount": e.amount,
        "category": e.category,
        "note": e.note,
        "date": e.date
    } for e in expenses], user_budget)
