import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///chatbot.db")
UPLOAD_DIR = os.path.join("data", "uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)
