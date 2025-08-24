import streamlit as st

# Check if user is logged in
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ You must log in first to access the chatbot.")
    st.stop()  # Stop rendering the page until login is done

st.title("💬 Chatbot")

# Example chatbot placeholder
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

user_input = st.text_input("You:", key="chat_input")

if st.button("Send"):
    if user_input:
        st.session_state["chat_history"].append(("You", user_input))
        # 🔥 Replace this with your LLM call later
        bot_response = f"Echo: {user_input}"
        st.session_state["chat_history"].append(("Bot", bot_response))

# Display chat history
for role, message in st.session_state["chat_history"]:
    if role == "You":
        st.markdown(f"**🧑 {role}:** {message}")
    else:
        st.markdown(f"**🤖 {role}:** {message}")
import streamlit as st  

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:  
    st.error("You need to login first to access this page.")  
    st.stop()
