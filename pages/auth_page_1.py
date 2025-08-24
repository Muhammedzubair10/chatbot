import os
import sqlite3
import streamlit as st

# ---------------- Database Setup ---------------- #
def init_db():
    # ✅ Ensure folder exists
    os.makedirs("database", exist_ok=True)

    # ✅ Connect to DB inside that folder
    conn = sqlite3.connect("database/users.db")
    c = conn.cursor()

    # ✅ Create users table if it doesn’t exist
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    email TEXT UNIQUE,
                    password TEXT
                )''')

    conn.commit()
    conn.close()

# Call this when page loads
init_db()

# ---------------- Signup Function ---------------- #
def signup_user(username, email, password):
    conn = sqlite3.connect("database/users.db")
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                  (username, email, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# ---------------- Login Function ---------------- #
def login_user(email, password):
    conn = sqlite3.connect("database/users.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()
    conn.close()
    return user

# ---------------- Streamlit UI ---------------- #
st.title("🔐 User Authentication")

menu = ["Signup", "Login"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Signup":
    st.subheader("Create New Account")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):
        if signup_user(username, email, password):
            st.success("✅ Account created successfully! Please login.")
        else:
            st.error("❌ Email already exists!")

elif choice == "Login":
    st.subheader("Login to Your Account")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = login_user(email, password)
        if user:
            st.success(f"✅ Welcome {user[1]}!")
        else:
            st.error("❌ Invalid email or password")
import streamlit as st

# After successful login
st.session_state["logged_in"] = True
st.session_state["user"] = email  # optional, store user email/name
st.success(f"Welcome {email}!")
