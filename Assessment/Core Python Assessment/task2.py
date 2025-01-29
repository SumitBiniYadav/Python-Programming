from task1 import *

obj = Fruit_Customer()

# Initial function for Initial transaction
print("Welcome To Fruit Market")
print(datetime.now())

# Display main menu options
menu1 = """
    1) Manager
    2) Customer  

"""
while True:
    print(menu1)
    choice = int(input("Select Your Role: "))

    if choice == 1:
        # Manager functionalities
        print("Fruit Market Manager")
        menu = """

            1) Add Fruit Stock
            2) View Fruit Stock

        """

        print(menu)
        choice1 = int(input("Enter Your Choice: "))

        if choice1 == 1:
            # Loop to allow adding multiple fruits
            while True:
                obj.add_fruit()
                more_fruit = input("Do you want to add more fruits? (y/n): ")
                if more_fruit != 'y':
                    break

        elif choice1 == 2:
            # View fruit stock
            obj.view_stock()

        else:
            print("Invalid Input! Try Again !!!")

    elif choice == 2:
        # Customer functionalities
        print("Fruit Market Customer")
        menu2 = """
                1) Buy Fruit
                2) Exit

        """
        print(menu2)
        choice2 = int(input("Enter Your Choice: "))

        if choice2 == 1:
            # Customer buying fruit
            obj.buy_fruit()
        else:
            print("Thanks For Visiting!!")
            break
    
    else:
        print("Invalid Input !")
        break
