import streamlit as st
from backend.auth import signup_user,login_user
from backend.db import init_db
from backend.utils import show_sidebar
from pages import chat_page,admin_page
from backend.db import init_db




# Initialize DB
init_db()

# Sidebar
show_sidebar()

# User authentication
if not signup_user():
    login_user()
else:
    # Navigation
    PAGES = {
        "Chat": chat_page,
        "Admin": admin_page,
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()


st.set_page_config(
    page_title="Grokish Chatbot",
    page_icon="🤖",
    layout="wide",
)

def main():
    st.title("🤖 Grokish Chatbot")

    # Ask for email login if not set
    if "user_id" not in st.session_state:
        st.subheader("Login to start chatting")
        email = st.text_input("Enter your email")
        if st.button("Login") and email:
            login_user(email)
            st.success("Logged in successfully! Use the sidebar to go to Chat.")
        return

    # Sidebar navigation
    st.sidebar.title("Navigation")
    st.sidebar.markdown("[💬 Chat](1_💬_Chat)")
    st.sidebar.markdown("[📊 Admin](2_📊_Admin)")

    st.sidebar.divider()
    st.sidebar.write(f"Logged in as: {st.session_state['email']}")

if __name__ == "__main__":
    main()
from pages import login_page
from pages import signup_page
from pages import chat_page
PAGES = {
    "Login": login_page.login_page,
    "Sign Up": signup_page.signup_page,
    "Chat Page": chat_page.chat_page,
}

st.sidebar.title("📍 Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page()
from backend.llm import chat_with_gemini

if prompt := st.chat_input("Type your message..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    bot_reply = chat_with_gemini(prompt, st.session_state.messages)

    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
