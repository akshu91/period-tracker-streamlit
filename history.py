import streamlit as st
from auth import load_users

def show_history(email):
    users = load_users()
    user_data = users.get(email, {}).get("data", [])
    if not user_data:
        st.info("No history available.")
    else:
        st.write("Your period history:")
        st.table(user_data)