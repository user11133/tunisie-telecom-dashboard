import sqlite3
import hashlib

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def add_admin(username, password):
    """Add a new admin to the database"""
    try:
        conn = sqlite3.connect("admins.db")
        c = conn.cursor()
        
        # Check if username already exists
        c.execute("SELECT COUNT(*) FROM admins WHERE username = ?", (username,))
        if c.fetchone()[0] > 0:
            print(f"Error: Admin '{username}' already exists")
            return False
        
        # Insert new admin
        password_hash = hash_password(password)
        c.execute(
            "INSERT INTO admins (username, password_hash) VALUES (?, ?)",
            (username, password_hash)
        )
        
        conn.commit()
        conn.close()
        print(f"Admin '{username}' added successfully!")
        return True
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

if __name__ == "__main__":
    print("=== Add New Admin ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    add_admin(username, password)