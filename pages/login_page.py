import streamlit as st
from backend.auth import login_user

def login_page():
    st.title("🔑 Login")

    st.write("Enter your credentials to access the chatbot.")

    with st.form("login_form"):
        email = st.text_input("📧 Email", placeholder="Enter your email")
        password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")

        submitted = st.form_submit_button("Login")

        if submitted:
            if not email or not password:
                st.warning("⚠️ Please fill in all fields.")
            else:
                try:
                    user = login_user(email, password)  # check DB
                    if user:
                        st.session_state["logged_in"] = True
                        st.session_state["user"] = user
                        st.success(f"✅ Welcome back, {user['username']}!")
                        st.info("Go to the Chat Page from the sidebar.")
                    else:
                        st.error("❌ Invalid email or password.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")
import streamlit as st

# After successful login
st.session_state["logged_in"] = True
st.session_state["user"] = email  # optional, store user email/name
st.success(f"Welcome {email}!")
