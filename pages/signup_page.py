import streamlit as st
from backend.auth import signup_user

def signup_page():
    st.title("📝 Sign Up")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if signup_user(email, password):
            st.success("Signup successful! ✅ Now you can login.")
        else:
            st.error("User already exists ❌")
