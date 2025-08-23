from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

with engine.begin() as conn:
    conn.execute(text("INSERT INTO users (username, password) VALUES (:u, :p)"),
                 {"u": "testuser", "p": "testpass"})

print("✅ Inserted test user successfully")
