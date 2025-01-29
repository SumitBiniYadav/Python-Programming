from datetime import datetime

#intial function for Intial transaction
def welcome():
    print("Welcome To Fruit Market")
    print(datetime.now())

#fruit manager module 
class Fruit_Manager:
    fruit_stock = {}

    def add_fruit(self):
        self.fruit = input("Enter Fruit Name : ")
        self.quantity = int(input("Enter the quantity to add : "))

        if self.fruit in self.fruit_stock:
            self.fruit_stock[self.fruit] += self.quantity
        
        else:
            self.fruit_stock[self.fruit] = self.quantity
        
        print(f"{self.quantity} {self.fruit} added sucessfully.")

    def view_stock(self):
        if not self.fruit_stock:
            print("No items Available In Fruit Stock !!")
        else:
            for self.fruit, self.quantity in self.fruit_stock.items():
                print(f"-{self.fruit}: {self.quantity}")

#class created that manages the Customer end of the prompt!!
class Fruit_Customer(Fruit_Manager):
    def buy_fruit(self):
        self.fruit = input("Enter the fruit name to buy: ")   
        if self.fruit in self.fruit_stock:
            self.quantity = int(input("Enter quantity to buy: "))
            if self.fruit_stock >= self.quantity:                   #if the quantity of the fruit purchased is leser than the qun in the fruit stock variable-
                    self.fruit_stock -= self.quantity               #reduce the quantity from the fruit stock of that particular fruit
                    print(f"You have sucessfully purchased {self.quantity} {self.fruit}")
                    if self.fruit_stock[self.fruit] == 0:            #condition if the fruit in the fruit stock becomes 0-
                        del self.fruit_stock[self.fruit]            #the fruit item will be deleted from the dict!
                    else:
                        print(f"Sorry only {self.quantity} {self.fruit} are available for sale!")
            else:
                print(f"Sorry,{self.fruit} is not available in stock for sale!")

