import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchPrediction } from "../redux/Slices.jsx/predictionSlice";


export default function Prediction() {
  const dispatch = useDispatch();
  const prediction = useSelector(state => state.prediction);

  useEffect(() => {
    dispatch(fetchPrediction());
  }, [dispatch]);

  if (!prediction) return null;

  return (
    <div style={{ marginTop: "20px" }}>
      <h2>Budget Prediction</h2>
      <p>Total spent: ${prediction.total_spent || 0}</p>
      <p>Daily average: ${prediction.daily_avg || 0}</p>
      <p>Projected total: ${prediction.projected_total || 0}</p>
      {prediction.alert && <p style={{ color: "red" }}>{prediction.alert}</p>}
    </div>
  );
}
