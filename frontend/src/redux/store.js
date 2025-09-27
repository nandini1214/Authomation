import { configureStore } from "@reduxjs/toolkit";
import expensesReducer from "./Slices.jsx/expensesSlice";
import budgetReducer from "./Slices.jsx/budgetSlice";
import predictionReducer from "./Slices.jsx/predictionSlice";


export const store = configureStore({
  reducer: {
    expenses: expensesReducer,
    budget: budgetReducer,
    prediction: predictionReducer,
  },
});
