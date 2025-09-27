import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { deleteExpense, fetchExpenses } from "../redux/Slices.jsx/expensesSlice";


export default function ExpenseList() {
  const dispatch = useDispatch();
  const expenses = useSelector(state => state.expenses);

  useEffect(() => {
    dispatch(fetchExpenses());
  }, [dispatch]);

  const handleDelete = (id) => {
    dispatch(deleteExpense(id));
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <h2>Expenses</h2>
      {expenses.length === 0 && <p>No expenses yet</p>}
      <ul>
        {expenses.map(exp => (
          <li key={exp.id}>
            {exp.date} - {exp.category} - ${exp.amount} - {exp.note}
            <button onClick={() => handleDelete(exp.id)} style={{ marginLeft: "10px" }}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
