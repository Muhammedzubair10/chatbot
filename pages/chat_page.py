# pages/chat_page.py
import streamlit as st

# Try to use your real LLM; fall back to echo if it's not available.
try:
    from backend.llm import generate_reply  # adjust if your function name differs
except Exception:
    def generate_reply(prompt: str, history: list[dict]) -> str:
        return f"Echo: {prompt}"

PAGE_TITLE = "💬 Chatbot"

def app():
    st.title(PAGE_TITLE)

    # --- Auth gate ---
    if not st.session_state.get("logged_in"):
        st.warning("You must log in first to access the chatbot.")
        st.stop()

    # --- Init chat history once ---
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm ready. Ask me anything."}
        ]

    # --- Sidebar tools ---
    with st.sidebar:
        if st.button("🧹 Clear chat"):
            st.session_state.messages = [
                {"role": "assistant", "content": "Chat cleared. How can I help?"}
            ]
            st.experimental_rerun()

        if st.button("🚪 Logout"):
            st.session_state["logged_in"] = False
            st.success("You have been logged out.")
            st.experimental_rerun()

    # --- Render history ---
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # --- One-shot input -> one-shot append ---
    if prompt := st.chat_input("Type your message…"):
        # 1) append user message exactly once
        st.session_state.messages.append({"role": "user", "content": prompt})

        # 2) generate reply once (LLM or echo)
        try:
            reply = generate_reply(prompt, st.session_state.messages)
        except Exception as e:
            reply = f"(fallback) Echo: {prompt}\n\n> Error calling LLM: {e}"

        # 3) append assistant reply once
        st.session_state.messages.append({"role": "assistant", "content": reply})

        # No extra appends, no loops. Streamlit rerun will just re-render the list above.

# Run when opened as a page
if __name__ == "__main__":
    app()
