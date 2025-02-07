import pymysql
from tkinter import *
# Establishing MySQL Connection
def connect_db():
    try:
        db = pymysql.connect(host="localhost", user="root", password="", database="Bank")
        cursor = db.cursor()
        return db, cursor
    except Exception as e:
        print("Error Connecting to Database:", e)
        return None, None

def signup():

    db, mycursor = connect_db()
    if not db:
        return

    name = input("Enter Your Name: ")
    email = input("Enter Email ID: ")

    while True:    
        mobile = input("Enter Mobile Number: ")
        if len(mobile) != 10 or not mobile.isdigit():
            print("Invalid Mobile Number! Try Again.")
            continue
        break

    while True:
        password = input("Enter Password: ")
        cpass = input("Confirm Password: ")

        if cpass == password:
            break
        else:
            print("Passwords Do Not Match! Try Again.")

    try:
        query = "INSERT INTO banker (bname, bemail, bmobile, bpass) VALUES (%s, %s, %s, %s)"
        mycursor.execute(query, (name, email, mobile, password))
        db.commit()
        print("SignUp Successful!")
    except Exception as e:
        print("Error:", e)
    finally:
        db.close()



def login():
    db, mycursor = connect_db()
    if not db:
        return

    while True:
        mobile = input("Enter Mobile Number: ")
        if len(mobile) != 10 or not mobile.isdigit():
            print("Invalid Mobile Number! Try Again.")
            continue
        break

    password = input("Enter Your Password: ")

    try:
        query = "SELECT bpass FROM banker WHERE bmobile = %s"
        mycursor.execute(query, (mobile,))
        user = mycursor.fetchone()

        if user and user[0] == password:
            print("Login Successful!")
        else:
            print("Invalid Mobile Number or Password! Try Again.")
    except Exception as e:
        print("Error:", e)
    finally:
        db.close()
