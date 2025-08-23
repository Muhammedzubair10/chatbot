import streamlit as st
from backend.auth import signup_user

def signup_page():
    st.title("🔐 Sign Up")

    st.write("Create a new account to access the chatbot.")

    with st.form("signup_form", clear_on_submit=True):
        username = st.text_input("👤 Username", placeholder="Enter your username")
        email = st.text_input("📧 Email", placeholder="Enter your email")
        password = st.text_input("🔑 Password", type="password", placeholder="Enter a strong password")

        submitted = st.form_submit_button("Sign Up")

        if submitted:
            if not username or not email or not password:
                st.warning("⚠️ Please fill in all fields.")
            else:
                try:
                    signup_user(username, email, password)  # save to DB
                    st.success("✅ Signup successful! Please log in now.")
                    st.info("Go to the login page to continue.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
