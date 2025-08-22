import streamlit as st
from backend.storage import get_all_users, get_all_chats

def admin_ui():
    # ✅ Check if logged in
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        st.warning("⚠️ You must log in as Admin first.")
        st.stop()

    # ✅ Check if user is admin
    if "role" not in st.session_state or st.session_state["role"] != "admin":
        st.error("🚫 You are not authorized to view this page.")
        st.stop()

    st.title("📊 Admin Dashboard")

    # Registered users
    st.subheader("Registered Users")
    try:
        users = get_all_users()
        if users:
            # 🔍 Search users by email
            search_user = st.text_input("Search user by email")
            if search_user:
                users = [u for u in users if search_user.lower() in u['email'].lower()]

            st.dataframe(users)
        else:
            st.info("No users found.")
    except Exception as e:
        st.error(f"Error loading users: {e}")

    # Chats
    st.subheader("All Chats")
    try:
        chats = get_all_chats()
        if chats:
            # 🔍 Search chats by user email
            search_chat = st.text_input("Search chats by email")
            if search_chat:
                chats = [c for c in chats if search_chat.lower() in c['email'].lower()]

            st.dataframe(chats)
        else:
            st.info("No chats found.")
    except Exception as e:
        st.error(f"Error loading chats: {e}")


# ✅ Call admin UI
admin_ui()
