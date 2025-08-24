import streamlit as st
from backend.db import init_db
from backend.utils import show_sidebar
from pages import login_page, signup_page, chat_page, admin_page

# Streamlit page config
st.set_page_config(
    page_title="🤖 Grokish Chatbot",
    page_icon="🤖",
    layout="wide",
)

# Initialize DB
init_db()

# Sidebar (optional custom items)
show_sidebar()

# Define available pages
PAGES = {
    "Login": login_page.login_page,
    "Sign Up": signup_page.signup_page,
    "Chat": chat_page.chat_page,
    "Admin": admin_page.admin_page,
}

# Sidebar Navigation
st.sidebar.title("📍 Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Run selected page
page = PAGES[selection]
page()
