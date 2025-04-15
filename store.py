import streamlit as st
from auth import load_users, save_users

def store_period_data(email):
    users = load_users()
    user_data = users.get(email, {}).get("data", [])

    date = st.date_input("Select date")
    if st.button("Save Date"):
        str_date = date.strftime("%Y-%m-%d")
        if str_date not in user_data:
            user_data.append(str_date)
            users[email]["data"] = user_data
            save_users(users)
            st.success("Date saved successfully!")
        else:
            st.info("Date already exists.")