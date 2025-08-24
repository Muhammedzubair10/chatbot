import google.generativeai as genai
from backend.config import GEMINI_API_KEY

# Configure API key
genai.configure(api_key=GEMINI_API_KEY)

# Use latest model
model = genai.GenerativeModel("gemini-1.5-flash")

def chat_with_gemini(prompt, history=[]):
    """
    Send message to Gemini with optional history.
    History should be a list of dicts like:
    [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi!"}]
    """
    # Convert history into Gemini format
    messages = []
    for msg in history:
        messages.append(f"{msg['role'].capitalize()}: {msg['content']}")

    # Add the new user prompt
    conversation = "\n".join(messages + [f"User: {prompt}"])

    # Generate response
    response = model.generate_content(conversation)
    return response.text

