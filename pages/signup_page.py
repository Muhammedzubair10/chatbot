import streamlit as st
from backend.auth import signup_user

def signup_page():
    st.title("📝 Sign Up Page")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if signup_user(username, email, password):
            st.success("Signup successful! Please go to the Login page.")
        else:
            st.error("Signup failed. Email may already exist.")
