# 🤖 AI Chatbot with Admin Dashboard  

## 📖 Project Overview  
This project is an **AI-powered chatbot system** built with **Streamlit**.  
It provides:  
- A **chat interface** powered by an LLM (Gemini/OpenAI).  
- A **user authentication system** to secure access.  
- An **admin dashboard** for managing users and monitoring chats.  
- A **database layer** to store user credentials and sessions.  

The goal of the project is to demonstrate a **complete end-to-end chatbot solution** with authentication, admin management, and a modular architecture.

---

## 🎯 Objectives  
1. Build a user-friendly **chatbot interface**.  
2. Implement **login/logout authentication** before accessing the chatbot.  
3. Provide an **admin page** to manage registered users.  
4. Integrate a **database** (SQLite/Postgres) for persistence.  
5. Deploy the chatbot app to a cloud platform.  

---

## 🏗️ System Architecture  

┌────────────────────────────┐
│ Frontend (UI) │
│ Streamlit Pages: │
│ • Login │
│ • Chatbot Interface │
│ • Admin Panel │
└─────────────┬──────────────┘
│
▼
┌────────────────────────────┐
│ Backend Logic │
│ • Authentication Handler │
│ • Chatbot Response Engine │
│ • Admin Management Logic │
└─────────────┬──────────────┘
│
▼
┌────────────────────────────┐
│ Database │
│ • User Credentials │
│ • Chat Logs (optional) │
│ • Admin Configurations │
└────────────────────────────┘

## 📂 Folder Structure  

├── app.py # Main entry point
├── admin_page.py # Admin dashboard
├── chat_page.py # Chat interface
├── init.py # Database initialization
├── backend/ # Database & logic files
├── requirements.txt # Dependencies
├── README.md # Project documentation


---

## ⚙️ Workflow  

1. **Initialization (`init.py`)**  
   - Creates the database.  
   - Defines tables for users, admins, and sessions.  

2. **Authentication (Login System)**  
   - User must log in before accessing chatbot.  
   - Session state is used to track login status.  

3. **Chatbot Interaction (`chat_page.py`)**  
   - Users type queries.  
   - Queries are sent to LLM backend (Gemini/OpenAI).  
   - Responses are displayed in chat window.  

4. **Admin Panel (`admin_page.py`)**  
   - Admin can view/manage users.  
   - Add/remove user accounts.  

5. **Deployment (`app.py`)**  
   - Streamlit serves as the entry point.  
   - Routes users to correct pages (login, chat, admin).  

---

## 🛠️ Technology Stack  

- **Frontend & UI:** Streamlit  
- **Backend Logic:** Python  
- **Database:** SQLite (local) or PostgreSQL (cloud)  
- **AI Model:** Gemini API / OpenAI API  
- **Deployment:** Streamlit Cloud / Render / Docker  

---

## ✅ Key Features  

- 🔒 **Login Authentication** → Only registered users can access chatbot.  
- 💬 **Interactive Chatbot** → Conversational AI responses in real time.  
- 🛡️ **Admin Page** → Manage users & settings.  
- 🗂️ **Database Support** → Store credentials & session data.  
- 🎨 **Dark Theme UI** → Clean and modern design.  

---

## 📌 Future Improvements  

- Add **chat history persistence** for users.  
- Implement **role-based access control (RBAC)**.  
- Improve **memory support** for chatbot.  
- Add **analytics dashboard** in admin panel.  
- Multi-language chatbot support.  

---

## 👨‍💻 Author  

Developed by **[Zubair]** ✨  
This project is open for contributions.  
