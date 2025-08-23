# backend/auth.py
from sqlalchemy import create_engine, text
from passlib.hash import bcrypt
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///chatbot.db")
engine = create_engine(DATABASE_URL, echo=False, future=True)


# ✅ Signup a new user
def signup_user(username: str, password: str) -> bool:
    hashed_pw = bcrypt.hash(password)
    try:
        with engine.begin() as conn:
            conn.execute(
                text("INSERT INTO users (username, password) VALUES (:u, :p)"),
                {"u": username, "p": hashed_pw},
            )
        return True
    except Exception as e:
        print(f"❌ Signup failed: {e}")
        return False


# ✅ Login user
def login_user(username: str, password: str) -> bool:
    with engine.begin() as conn:
        result = conn.execute(
            text("SELECT password FROM users WHERE username = :u"),
            {"u": username}
        ).fetchone()

    if result and bcrypt.verify(password, result[0]):
        return True
    return False


# ✅ Check if user exists
def user_exists(username: str) -> bool:
    with engine.begin() as conn:
        result = conn.execute(
            text("SELECT 1 FROM users WHERE username = :u"),
            {"u": username}
        ).fetchone()
    return result is not None
