import pymysql

# Connect to MySQL server
mydb = pymysql.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor()

# Create Database if it does not exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS Bank")
mydb.commit()

# Reconnect to the 'Bank' database
mydb = pymysql.connect(host="localhost", user="root", password="", database="Bank")
mycursor = mydb.cursor()

# Create Banker table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Banker (
        bid INT PRIMARY KEY AUTO_INCREMENT,
        bname VARCHAR(80) CHARACTER SET utf8mb4 NOT NULL,
        bmobile BIGINT UNIQUE KEY NOT NULL,
        bpass VARCHAR(80) NOT NULL
    )
""")
mydb.commit()

# Create Customer table with foreign key reference to Banker
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Customer (
        cid INT PRIMARY KEY AUTO_INCREMENT,
        cname VARCHAR(80) CHARACTER SET utf8mb4 NOT NULL,
        cmobile BIGINT UNIQUE KEY NOT NULL,
        cpass VARCHAR(80) NOT NULL,
        balance DECIMAL(10,2) DEFAULT 0.00,
        bid INT,
        FOREIGN KEY (bid) REFERENCES Banker (bid) ON DELETE CASCADE
    )
""")
mydb.commit()

print("Database and Tables Created Successfully!")
