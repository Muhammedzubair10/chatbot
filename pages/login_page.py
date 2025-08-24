import streamlit as st
from backend.auth import login_user

def login_page():
    st.title("🔑 Login Page")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = login_user(email, password)
        if user:
            st.session_state["user"] = email   # store logged-in user
            st.success(f"Welcome back, {email}!")
        else:
            st.error("Invalid email or password")
