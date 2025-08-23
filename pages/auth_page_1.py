import streamlit as st
import sqlite3
import hashlib

# ---------- DB Setup ----------
def init_db():
    conn = sqlite3.connect("database/users.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup_user(username, email, password):
    conn = sqlite3.connect("database/users.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users(username, email, password) VALUES (?, ?, ?)",
                  (username, email, hash_password(password)))
        conn.commit()
        st.success("✅ Account created successfully! Please login.")
    except sqlite3.IntegrityError:
        st.error("⚠️ Username or Email already exists.")
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect("database/users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?",
              (username, hash_password(password)))
    data = c.fetchone()
    conn.close()
    return data

# ---------- Streamlit UI ----------
def main():
    st.markdown(
        """
        <style>
        .main {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .auth-card {
            background: #1e1e1e;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
            width: 350px;
            text-align: center;
        }
        .stTextInput>div>div>input {
            background: #2d2d2d;
            color: white;
            border-radius: 10px;
        }
        .stButton>button {
            background: #4CAF50;
            color: white;
            border-radius: 10px;
            width: 100%;
        }
        .stTabs [role="tab"] {
            padding: 10px 20px;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
    st.title("🔐 Chatbot Portal")

    tab1, tab2 = st.tabs(["🔑 Login", "📝 Sign Up"])

    with tab1:
        st.subheader("Login to your Account")
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            user = login_user(username, password)
            if user:
                st.session_state["logged_in"] = True
                st.session_state["username"] = user[1]
                st.success(f"✅ Welcome {user[1]}! Go to Chat Page.")
            else:
                st.error("❌ Invalid Username or Password")

    with tab2:
        st.subheader("Create New Account")
        username = st.text_input("Username", key="signup_user")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_pass")
        if st.button("Sign Up"):
            if username and email and password:
                signup_user(username, email, password)
            else:
                st.warning("⚠️ Please fill all fields.")

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    init_db()
    main()
import streamlit as st
from backend.auth import signup_user, login_user

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = None

st.title("🔐 Authentication Page")

tab1, tab2 = st.tabs(["Login", "Signup"])

# --- LOGIN TAB ---
with tab1:
    st.subheader("Login to your account")

    login_email = st.text_input("Email", key="login_email")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        if login_user(login_email, login_password):
            st.session_state.logged_in = True
            st.session_state.user_email = login_email
            st.success("✅ Logged in successfully!")
            
        else:
            st.error("❌ Invalid email or password")

# --- SIGNUP TAB ---
with tab2:
    st.subheader("Create a new account")

    signup_username = st.text_input("Username", key="signup_username")
    signup_email = st.text_input("Email", key="signup_email")
    signup_password = st.text_input("Password", type="password", key="signup_password")

    if st.button("Signup"):
        if signup_user(signup_username, signup_email, signup_password):
            st.success("🎉 Account created successfully! Please login now.")
        else:
            st.error("⚠️ Email already exists. Try logging in.")
