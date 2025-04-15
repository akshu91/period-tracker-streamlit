import streamlit as st
from datetime import datetime, timedelta
from mongo_utils import store_data, get_history

# --- Styling ---
st.set_page_config(page_title="Period Tracker", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-image: url("https://i.imgur.com/IgW9fKO.png");
        background-size: cover;
    }
    .main {
        background-color: rgba(255, 182, 193, 0.3);
        padding: 2rem;
        border-radius: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main">', unsafe_allow_html=True)

# --- Title ---
st.title("🌸 Period Tracker")

menu = st.sidebar.radio("Menu", ["Predict", "Store My Data", "View History"])
username = st.sidebar.text_input("Enter your username", key="user")

if username.strip() == "":
    st.warning("Please enter your username in the sidebar to continue.")
else:
    if menu == "Store My Data":
        st.subheader("📝 Store Period Data")
        start_date = st.date_input("Start Date of Last Period")
        cycle_length = st.number_input("Cycle Length (in days)", min_value=20, max_value=40, value=28)
        period_length = st.number_input("Period Length (in days)", min_value=1, max_value=10, value=5)

        if st.button("Save Data"):
            store_data(username, str(start_date), cycle_length, period_length)
            st.success("Data saved successfully!")

    elif menu == "Predict":
        st.subheader("🔮 Predict Next Cycle")
        history = get_history(username)
        if not history:
            st.info("No data found. Please store your data first.")
        else:
            latest = history[-1]
            last_date = datetime.strptime(latest['start_date'], "%Y-%m-%d")
            next_start = last_date + timedelta(days=latest['cycle_length'])
            next_end = next_start + timedelta(days=latest['period_length'])
            st.write(f"Next Expected Period: **{next_start.strftime('%d %B %Y')}** to **{next_end.strftime('%d %B %Y')}**")

    elif menu == "View History":
        st.subheader("📚 Period History")
        history = get_history(username)
        if not history:
            st.info("No history available.")
        else:
            for entry in reversed(history):
                st.write(f"- **Date**: {entry['start_date']}, **Cycle**: {entry['cycle_length']} days, **Length**: {entry['period_length']} days")

st.markdown('</div>', unsafe_allow_html=True)
