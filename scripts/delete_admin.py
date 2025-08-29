import sqlite3

def delete_admin(username):
    """Delete an admin from the database"""
    try:
        conn = sqlite3.connect("admins.db")
        c = conn.cursor()
        
        # Prevent deleting the last admin
        c.execute("SELECT COUNT(*) FROM admins")
        admin_count = c.fetchone()[0]
        
        if admin_count <= 1:
            print("Error: Cannot delete the last admin")
            return False
        
        # Delete the admin
        c.execute("DELETE FROM admins WHERE username = ?", (username,))
        
        if c.rowcount == 0:
            print(f"Error: Admin '{username}' not found")
            return False
        
        conn.commit()
        conn.close()
        print(f"Admin '{username}' deleted successfully!")
        return True
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

if __name__ == "__main__":
    print("=== Delete Admin ===")
    username = input("Enter username to delete: ")
    
    delete_admin(username)