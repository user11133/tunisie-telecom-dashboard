import sqlite3

def view_admins():
    """View all admins in the database"""
    try:
        conn = sqlite3.connect("admins.db")
        c = conn.cursor()
        
        c.execute("SELECT id, username, created_at FROM admins ORDER BY created_at DESC")
        admins = c.fetchall()
        
        print("=== List of Admins ===")
        for admin in admins:
            print(f"ID: {admin[0]}, Username: {admin[1]}, Created: {admin[2]}")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    view_admins()