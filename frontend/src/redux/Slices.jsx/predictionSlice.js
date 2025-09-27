import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

const API_URL = "http://127.0.0.1:8000";

export const fetchPrediction = createAsyncThunk("prediction/fetch", async () => {
  const res = await fetch(`${API_URL}/budget/predict`);
  return res.json();
});

const predictionSlice = createSlice({
  name: "prediction",
  initialState: null,
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(fetchPrediction.fulfilled, (state, action) => action.payload);
  },
});

export default predictionSlice.reducer;
