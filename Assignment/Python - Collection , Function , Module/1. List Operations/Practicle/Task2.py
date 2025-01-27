my_list = ["apple", "banana", "cherry",True,False,1,3,5]
print("Initial list:", my_list)


# Removing elements using pop()
removed_element = my_list.pop()  # Removes the last element
print(f"After popping the last element ('{removed_element}'):", my_list)

# Removing elements using remove()
my_list.remove("banana")  # Removes 'banana' from the list
print("After removing 'banana':", my_list)