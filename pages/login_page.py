import streamlit as st
from backend.auth import login_user

def login_page():
    st.title("🔑 Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login_user(email, password):
            st.session_state["user"] = email
            st.success("Login successful! 🎉")
        else:
            st.error("Invalid credentials ❌")
