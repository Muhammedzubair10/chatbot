import streamlit as st

def signup_page():
    st.subheader("📝 Sign Up Page")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        st.session_state["user"] = email
        st.success(f"Account created for {email}!")
