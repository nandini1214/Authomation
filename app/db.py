from sqlalchemy import create_engine, Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./expenses.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Expense Table
class ExpenseDB(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String, default="Misc")
    note = Column(String, nullable=True)
    date = Column(Date)

# Budget Table
class BudgetDB(Base):
    __tablename__ = "budget"
    id = Column(Integer, primary_key=True)
    budget = Column(Float, nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)
