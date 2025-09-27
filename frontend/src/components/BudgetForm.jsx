import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { setBudget } from "../redux/Slices.jsx/budgetSlice";


export default function BudgetForm() {
  const [budgetValue, setBudgetValue] = useState("");
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(setBudget(parseFloat(budgetValue)));
    setBudgetValue("");
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginTop: "20px" }}>
      <input
        type="number"
        placeholder="Set Budget"
        value={budgetValue}
        onChange={e => setBudgetValue(e.target.value)}
        required
      />
      <button type="submit">Set Budget</button>
    </form>
  );
}
