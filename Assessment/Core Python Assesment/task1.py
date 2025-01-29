fruit_stock = {}

def add_stock():
    fruit = input("Enter Fruit Name: ")
    quantity = int(input("Enter the quantity to add: "))

    if fruit in fruit_stock:
        fruit_stock[fruit] += quantity
    else:
        fruit_stock[fruit] = quantity

    print(f"{quantity} {fruit} added successfully!!!")

def view_stock():  
    if not fruit_stock:
        print("No items available in Fruit Stock!!")
    else:
        print("Current Fruit Stock")
        for fruit, quantity in fruit_stock.items():
            print(f"{fruit}: {quantity}")

def buy_stock():
    fruit = input("Enter Fruit to Buy: ")
    if fruit in fruit_stock:
        quantity = int(input("Enter Quantity to Buy: "))

        if fruit_stock[fruit] >= quantity:
            fruit_stock[fruit] -= quantity
            print(f"Successful purchase: {quantity} {fruit}")

            if fruit_stock[fruit] == 0:
                del fruit_stock[fruit]
        else:
            print(f"Sorry, only {fruit_stock[fruit]} {fruit} is available for sale!")
    else:
        print(f"Sorry, {fruit} is not available in stock for sale!")

