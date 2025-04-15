import os
import json

SESSION_FILE = "session.json"

def save_user_session(email):
    with open(SESSION_FILE, "w") as f:
        json.dump({"user": email}, f)

def load_user_session():
    import streamlit as st
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            data = json.load(f)
            st.session_state.user = data.get("user")

def clear_user_session():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)