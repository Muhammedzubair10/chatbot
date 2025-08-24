import streamlit as st
from backend.db import init_db
from pages import login_page, signup_page, chat_page, admin_page

# -------------------------------
# Initialize Database
# -------------------------------
init_db()

# -------------------------------
# Streamlit Page Setup
# -------------------------------
st.set_page_config(
    page_title="Grokish Chatbot",
    page_icon="🤖",
    layout="wide",
)

# -------------------------------
# Define Navigation Pages
# -------------------------------
PAGES = {
    "Login": login_page.login_page,
    "Sign Up": signup_page.signup_page,
    "Chat": chat_page.chat_page,
    "Admin": admin_page.admin_page,
}

# -------------------------------
# Sidebar Navigation
# -------------------------------
st.sidebar.title("📍 Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Run Selected Page
page = PAGES[selection]
page()

# -------------------------------
# Show User Status if Logged In
# -------------------------------
if "user" in st.session_state and st.session_state["user"]:
    st.sidebar.divider()
    st.sidebar.success(f"👤 Logged in as: {st.session_state['user']}")
