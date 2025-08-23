from sqlalchemy import text
from backend.db import engine

def save_chat(user_id, role, message):
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO chats (user_id, role, message) VALUES (:uid, :role, :msg)"),
            {"uid": user_id, "role": role, "msg": message},
        )

def get_chat_history(user_id, limit=20):
    with engine.begin() as conn:
        rows = conn.execute(
            text("SELECT role, message FROM chats WHERE user_id=:uid ORDER BY id DESC LIMIT :limit"),
            {"uid": user_id, "limit": limit},
        ).fetchall()
    return [{"role": r[0], "parts": [r[1]]} for r in reversed(rows)]

import sqlite3

DB_PATH = "chatbot.db"

def get_all_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, email, created_at FROM users")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "email": r[1], "created_at": r[2]} for r in rows]


def get_all_chats():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT users.email, chats.role, chats.parts, chats.timestamp "
                   "FROM chats JOIN users ON chats.user_id = users.id "
                   "ORDER BY chats.timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return [{"email": r[0], "role": r[1], "parts": r[2], "timestamp": r[3]} for r in rows]
