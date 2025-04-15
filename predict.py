import streamlit as st
import datetime
from auth import load_users, save_users

def predict_next_period(email):
    users = load_users()
    user_data = users.get(email, {}).get("data", [])

    if len(user_data) < 2:
        st.warning("Need at least 2 data points to predict.")
        return

    dates = sorted([datetime.datetime.strptime(d, "%Y-%m-%d") for d in user_data])
    gaps = [(dates[i+1] - dates[i]).days for i in range(len(dates)-1)]
    avg_gap = sum(gaps) // len(gaps)
    next_date = dates[-1] + datetime.timedelta(days=avg_gap)

    st.success(f"Predicted next period: {next_date.strftime('%Y-%m-%d')}")