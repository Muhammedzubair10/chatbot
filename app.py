import streamlit as st
from backend.db import init_db
from pages import login_page, signup_page, chat_page, admin_page

# Initialize DB
init_db()

# Streamlit page setup
st.set_page_config(
    page_title="Grokish Chatbot",
    page_icon="🤖",
    layout="wide",
)

# Navigation pages
PAGES = {
    "Login": login_page.login_page,
    "Sign Up": signup_page.signup_page,
    "Chat": chat_page.chat_page,
    "Admin": admin_page.admin_page,
}

# Sidebar navigation
st.sidebar.title("📍 Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Run selected page
page = PAGES[selection]
page()

# If user is logged in, show status
if "user" in st.session_state:
    st.sidebar.divider()
    st.sidebar.write(f"👤 Logged in as: {st.session_state['user']}")
