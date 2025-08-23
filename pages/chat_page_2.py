import streamlit as st

st.title("💬 Chat Page")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ You must log in first to access the chatbot.")
    st.stop()

st.success(f"Welcome {st.session_state['username']}! Start chatting...")
