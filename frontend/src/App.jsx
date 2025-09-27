
import AddExpense from "./components/AddExpenses";
import BudgetForm from "./components/BudgetForm";
import ExpenseList from "./components/ExpenseList";
import Prediction from "./components/Prediction";


export default function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Smart Budget App with Redux</h1>
      <BudgetForm />
      <AddExpense />
      <ExpenseList />
      <Prediction />
    </div>
  );
}
