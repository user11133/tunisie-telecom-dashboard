import streamlit as st
import hashlib
import sqlite3
import os

# Database file
DB_FILE = "admins.db"

def init_db():
    """Initialize the database with admins table"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # Create admins table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create default admin user if it doesn't exist
    c.execute("SELECT COUNT(*) FROM admins WHERE username = 'admin'")
    if c.fetchone()[0] == 0:
        admin_password_hash = hash_password("admin123")
        c.execute(
            "INSERT INTO admins (username, password_hash) VALUES (?, ?)",
            ('admin', admin_password_hash)
        )
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Get a database connection"""
    return sqlite3.connect(DB_FILE)

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_admin(username, password):
    """Authenticate an admin"""
    try:
        conn = get_db_connection()
        c = conn.cursor()
        
        # Get admin data
        c.execute(
            "SELECT username, password_hash FROM admins WHERE username = ?",
            (username,)
        )
        admin = c.fetchone()
        conn.close()
        
        if not admin:
            return False, "Admin not found"
        
        stored_hash = admin[1]
        if stored_hash != hash_password(password):
            return False, "Incorrect password"
        
        return True, "Authentication successful"
    
    except sqlite3.Error as e:
        return False, f"Database error: {e}"

def init_auth_session_state():
    """Initialize authentication session state"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'show_login' not in st.session_state:
        st.session_state.show_login = True

# Initialize the database when this module is imported
init_db()