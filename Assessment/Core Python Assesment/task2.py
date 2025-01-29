from task1 import * 
from datetime import datetime

menu = """
    **** Select Role ****
    1) Manager
    2) Customer
    3) Exit

"""

print("Welcome To Fruit Market")
print(datetime.now())


while True:
    print(menu)
    choice = int(input("Enter Your Role: "))

    if choice == 1:
        print('Fruit Market Manager')
        menu1 = """
        1) Add Fruit Stock
        2) View Fruit Stock
        """

        print(menu1)
        choice1 = int(input("Enter Your Choice: "))

        if choice1 == 1:
            while True: 
                add_stock()
                more_fruit = input("Do you want to order more (y/n): ")
                if more_fruit != 'y':
                    break

        elif choice1 ==2:
            view_stock()

        else:
            print("Invalid Input! Try Again !!!")


    elif choice == 2:
        print("Fruit Market Customer")
        menu2 = """
        1) Buy Fruit 
        2) Exit
        """

        print(menu2)
        choice2 = int(input("Enter Your Choice: "))

        if choice2 == 1:
            while True:
                buy_stock()
                buyMore = input("Do you want Buy More (y/n): ")
                if buyMore != 'y':
                    break
        else:
            print("Thank You! Please Visit Again!")

    elif choice == 3:
        print("Thank You!!")
        break

    else:
        print("Invalid Input!! Please enter a number between 1 and 3.")
        

