# Open the file in read mode
with open("sample.txt", "r") as file:
    print("Initial cursor position:", file.tell())  # Should be 0 at the beginning

    # Read some characters
    data = file.read(10)  # Read the first 10 characters
    print("After reading 10 characters, cursor position:", file.tell())

    # Read more data
    data = file.read(5)  # Read the next 5 characters
    print("After reading 5 more characters, cursor position:", file.tell())
