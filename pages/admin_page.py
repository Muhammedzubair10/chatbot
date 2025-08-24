import streamlit as st

def admin_page():
    st.title("📊 Admin Dashboard")

    # Check if user is logged in
    if "user" not in st.session_state:
        st.warning("⚠️ You need to login first to access the Admin page.")
        return

    # Restrict access to only admin
    if st.session_state["user"] != "admin@example.com":
        st.error("🚫 Access Denied! Only admin can view this page.")
        return

    # Admin content
    st.success("✅ Welcome Admin! You have full access.")

    st.subheader("📌 Admin Tools")
    st.write("- View registered users")
    st.write("- Monitor chatbot logs")
    st.write("- Manage database entries")
    st.write("- Update API settings")
