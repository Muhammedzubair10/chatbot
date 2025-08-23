import google.generativeai as genai
from backend.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")

def chat_with_gemini(prompt, history=[]):
    """Send message to Gemini with optional history."""
    response = model.generate_content([*history, {"role": "user", "parts": [prompt]}])
    return response.text
