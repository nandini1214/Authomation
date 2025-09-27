import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

const API_URL = "http://127.0.0.1:8000";

export const setBudget = createAsyncThunk("budget/set", async (budget) => {
  const res = await fetch(`${API_URL}/budget`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ budget }),
  });
  const data = await res.json();
  return data.message; // or return budget value if you want
});

const budgetSlice = createSlice({
  name: "budget",
  initialState: 0,
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(setBudget.fulfilled, (state, action) => state = action.payload);
  },
});

export default budgetSlice.reducer;
