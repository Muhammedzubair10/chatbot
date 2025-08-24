import streamlit as st
from backend.llm import chat_with_gemini

def chat_page():
    st.title("💬 Chat with Grokish Bot")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display chat history
    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input
    if prompt := st.chat_input("Type your message..."):
        st.chat_message("user").markdown(prompt)
        st.session_state["messages"].append({"role": "user", "content": prompt})

        bot_reply = chat_with_gemini(prompt, st.session_state["messages"])
        with st.chat_message("assistant"):
            st.markdown(bot_reply)
        st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
