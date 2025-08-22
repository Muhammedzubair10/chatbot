# frontend/app_auth_ui.py
import streamlit as st
from backend.auth import signup_user, login_user, user_exists
from backend.utils import show_sidebar

# ✅ Define app pages
def chat_page():
    st.title("💬 Chatbot")
    st.write("Welcome to the chatbot interface.")
    msg = st.text_input("Ask me something:")
    if st.button("Send"):
        st.write(f"You said: {msg}")  # later replace with LLM response

def admin_page():
    st.title("🛠 Admin Panel")
    st.write("Only accessible by admin.")
    st.write("Here you can manage users, view logs, etc.")

# ✅ Main App
def main():
    st.set_page_config(page_title="AI Chatbot", layout="wide")

    # Show sidebar with login/signup
    show_sidebar((signup_user, login_user, user_exists))

    # Check if user is logged in
    if "user" not in st.session_state:
        st.warning("⚠ Please login to continue.")
        return

    # Page navigation
    st.sidebar.subheader("📂 Navigation")
    page = st.sidebar.radio("Go to", ["Chat", "Admin"] if st.session_state["user"] == "admin" else ["Chat"])

    if page == "Chat":
        chat_page()
    elif page == "Admin":
        admin_page()

if __name__ == "__main__":
    main()
