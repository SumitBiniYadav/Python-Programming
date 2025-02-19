import sqlite3

def connect_db():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor):
    # Create a table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL)''')

def main():
    conn, cursor = connect_db()
    create_table(cursor)
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
