import pymysql

# Function to connect to the MySQL database
def connect_db():
    return pymysql.connect(host="localhost", user="root", password="", database="Bank")

# Class for Banker operations
class Bank:
    # Function to register a banker
    def register_banker(self):
        db = connect_db()
        cursor = db.cursor()
        
        self.bname = input("Enter Your Name: ")
        bmobile = input("Enter Mobile Number: ")
        
        # Check for valid mobile number
        if len(bmobile) != 10:
            print("Invalid Mobile Number! Try Again!!")
            return
        
        while True:
            self.bpassword = input("Create Password: ")
            self.confirm_pass = input("Confirm Your Password: ")

            # Check if passwords match
            if self.confirm_pass == self.bpassword:
                try:
                    cursor.execute("INSERT INTO Banker (bname, bmobile, bpass) VALUES (%s, %s, %s)", (self.bname, bmobile, self.bpassword))
                    db.commit()
                    print("Banker Registration Successful!")
                    break
                except pymysql.MySQLError as e:
                    print("Error:", e)
                finally:
                    db.close()
            else:
                print("Confirm password does not match! Retry!!")

    # Function to handle banker login
    def login_banker(self):
        db = connect_db()
        cursor = db.cursor()

        mobile = input("Enter Mobile Number: ")
        password = input("Enter Password: ")

        cursor.execute("SELECT * FROM Banker WHERE bmobile=%s AND bpass=%s", (mobile, password))
        banker = cursor.fetchone()
        db.close()

        if banker: 
            print(f"Welcome {banker[1]}!")
            self.banker_menu(banker[0])  # Redirect to banker menu
        else:
            print("Invalid Credentials!")

    # Function to display the banker menu
    def banker_menu(self, bid):
        while True:
            menu = """
            1) View All Customers
            2) Update Customer 
            3) Delete Customer 
            4) LogOut
            """
            print(menu)

            choice = input("Enter Your Choice: ")

            if choice == '1':
                self.view_customers()
            elif choice == '2':
                self.update_customer()
            elif choice == '3':
                self.delete_customer()
            elif choice == '4':
                break
            else:
                print("Invalid Input !!")

    # Function to view all customers
    def view_customers(self):
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Customer")
        customers = cursor.fetchall()
        db.close()

        for c in customers:
            print(f"ID: {c[0]}, Name: {c[1]}, Mobile: {c[2]}, Balance: {c[4]}")

    # Function to update a customer's details
    def update_customer(self):
        db = connect_db()
        cursor = db.cursor()
        cid = input("Enter Customer ID to Update: ")
        new_name = input("Enter New Name: ")
        cursor.execute("UPDATE Customer SET cname=%s WHERE cid=%s", (new_name, cid))
        db.commit()
        db.close()
        print("Customer Updated Successfully!!")

    # Function to delete a customer
    def delete_customer(self):
        db = connect_db()
        cursor = db.cursor()
        while True:
            cid = input("Enter Customer ID to delete: ")
            con_delete = input("Are You Sure, This will permanently delete the information (y/n): ")
            if con_delete == 'y':
                cursor.execute("DELETE FROM Customer WHERE cid=%s", (cid,))
                db.commit()
                db.close()
                print("Customer Deleted Successfully!!")
                break
            else:
                continue

# Class for Customer operations
class Customer:
    # Function to register a new customer
    def register_customer(self):
        db = connect_db()
        cursor = db.cursor()
        
        name = input("Enter Your Name: ")
        while True:
            mobile = input("Enter Mobile Number: ")
            if len(mobile) != 10:
                print("Invalid Mobile Number! Retry!")
                continue
            break

        password = input("Enter Your Unique Password: ")
        bid = input("Enter Banker ID: ")

        try:
            cursor.execute("INSERT INTO Customer (cname, cmobile, cpass, bid) VALUES (%s, %s, %s, %s)", (name, mobile, password, bid))
            db.commit()
            print("Customer Registered Successfully!!")
        except pymysql.MySQLError as e:
            print("Error:", e)
        finally:
            db.close()

    # Function to handle customer login
    def customer_login(self):
        db = connect_db()
        cursor = db.cursor()
        mobile = input("Enter Mobile Number: ")
        password = input("Enter Your Password: ")

        cursor.execute("SELECT * FROM Customer WHERE cmobile=%s AND cpass=%s", (mobile, password))
        customer = cursor.fetchone()
        db.close()

        if customer:
            print(f"Welcome {customer[1]}!")
            self.customer_menu(customer[0])  # Redirect to customer menu
        else:
            print("Invalid Credentials!!")

    # Function to display the customer menu
    def customer_menu(self, cid):
        while True:
            menu = """
            1) Deposit
            2) Withdraw 
            3) View Balance 
            4) Logout
            """
            print(menu)

            choice = input("Enter Your Choice: ")
            if choice == '1':
                self.deposit(cid)
            elif choice == '2':
                self.withdraw(cid)
            elif choice == '3':
                self.view_balance(cid)
            elif choice == '4':
                break
            else:
                print("Invalid Choice! Try Again!!")

    # Function to deposit money
    def deposit(self, cid):
        db = connect_db()
        cursor = db.cursor()
        amount = float(input("Enter Amount to Deposit: "))
        cursor.execute("UPDATE Customer SET balance = balance + %s WHERE cid = %s", (amount, cid))
        db.commit()
        db.close()
        print("Amount Deposited !!")

    # Function to withdraw money
    def withdraw(self, cid):
        db = connect_db()
        cursor = db.cursor()
        amount = float(input("Enter Amount to Withdraw: "))
        cursor.execute("UPDATE Customer SET balance = balance - %s WHERE cid = %s", (amount, cid))
        db.commit()
        db.close()
        print("Amount Withdrawn !!")

    # Function to view account balance
    def view_balance(self, cid):
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT balance FROM Customer WHERE cid=%s", (cid,))
        balance = cursor.fetchone()
        db.close()
        print(f"Your Balance: {balance[0]}")
