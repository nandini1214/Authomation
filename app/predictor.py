from datetime import date

def predict_budget(expenses, user_budget):
    today = date.today()
    days_passed = today.day
    days_in_month = 30  # simple estimate

    total_spent = sum(e["amount"] for e in expenses if e["date"].month == today.month)
    avg_per_day = total_spent / days_passed if days_passed else 0
    projected_total = avg_per_day * days_in_month

    alert = None
    if projected_total > user_budget and avg_per_day > 0:
        overuse_day = int(user_budget / avg_per_day)
        alert = f"At this rate, you'll exceed your budget by day {overuse_day} of the month."

    return {
        "total_spent": total_spent,
        "daily_avg": round(avg_per_day, 2),
        "projected_total": round(projected_total, 2),
        "budget": user_budget,
        "alert": alert
    }
