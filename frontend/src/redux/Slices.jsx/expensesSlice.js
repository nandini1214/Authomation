import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

const API_URL = "http://127.0.0.1:8000";

export const fetchExpenses = createAsyncThunk("expenses/fetch", async () => {
  const res = await fetch(`${API_URL}/expenses`);
  return res.json();
});

export const addExpense = createAsyncThunk("expenses/add", async (expense) => {
  const res = await fetch(`${API_URL}/expenses`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(expense),
  });
  return res.json();
});

export const deleteExpense = createAsyncThunk("expenses/delete", async (id) => {
  await fetch(`${API_URL}/expenses/${id}`, { method: "DELETE" });
  return id;
});

const expensesSlice = createSlice({
  name: "expenses",
  initialState: [],
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchExpenses.fulfilled, (state, action) => action.payload)
      .addCase(addExpense.fulfilled, (state, action) => [...state, action.payload])
      .addCase(deleteExpense.fulfilled, (state, action) => state.filter(e => e.id !== action.payload));
  },
});

export default expensesSlice.reducer;
