# backend/utils.py
import streamlit as st
import os
import datetime



def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_upload(file, upload_dir="data/uploads"):
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.name)
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    return file_path

# ✅ Sidebar for login/signup
def show_sidebar(auth_funcs):
    signup_user, login_user, user_exists = auth_funcs

    st.sidebar.header("🔐 Authentication")

    choice = st.sidebar.radio("Choose", ["Login", "Signup"])

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if choice == "Signup":
        if st.sidebar.button("Create Account"):
            if user_exists(username):
                st.sidebar.error("❌ Username already exists.")
            else:
                if signup_user(username, password):
                    st.sidebar.success("✅ Account created. Please login.")
                else:
                    st.sidebar.error("❌ Signup failed.")

    elif choice == "Login":
        if st.sidebar.button("Login"):
            if login_user(username, password):
                st.session_state["user"] = username
                st.sidebar.success(f"✅ Welcome {username}!")
            else:
                st.sidebar.error("❌ Invalid credentials")

    # ✅ If logged in, show logout
    if "user" in st.session_state:
        if st.sidebar.button("Logout"):
            st.session_state.pop("user")
            st.sidebar.success("👋 Logged out successfully!")
