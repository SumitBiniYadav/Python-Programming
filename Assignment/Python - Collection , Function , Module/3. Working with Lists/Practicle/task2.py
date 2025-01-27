# Sort a list using sort() and sorted()
unsorted_list = [5, 3, 8, 1, 2]

# Using sort() - this modifies the original list
print("\nOriginal list (before sort):", unsorted_list)
unsorted_list.sort()
print("List after sort() method:", unsorted_list)


# Using sorted() - this creates a new sorted list
another_unsorted_list = [7, 4, 6, 9, 1]
print("\nOriginal list (before sorted()):", another_unsorted_list)
sorted_list = sorted(another_unsorted_list)