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

def insert_data(cursor, conn, name, age):
    # Insert data into the table
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

def fetch_data(cursor):
    # Fetch data from the table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    return rows

def main():
    conn, cursor = connect_db()
    create_table(cursor)
    
    # Insert sample data
    insert_data(cursor, conn, "Alice", 25)
    insert_data(cursor, conn, "Bob", 30)
    
    # Fetch and print data
    users = fetch_data(cursor)
    for user in users:
        print(user)
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
