import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { addExpense } from "../redux/Slices.jsx/expensesSlice";


export default function AddExpense() {
  const [amount, setAmount] = useState("");
  const [category, setCategory] = useState("");
  const [note, setNote] = useState("");
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(addExpense({
      amount: parseFloat(amount),
      category,
      note,
      date: new Date().toISOString().split("T")[0]
    }));
    setAmount(""); setCategory(""); setNote("");
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginTop: "20px" }}>
      <input placeholder="Amount" value={amount} onChange={e => setAmount(e.target.value)} required />
      <input placeholder="Category" value={category} onChange={e => setCategory(e.target.value)} required />
      <input placeholder="Note" value={note} onChange={e => setNote(e.target.value)} />
      <button type="submit">Add Expense</button>
    </form>
  );
}
