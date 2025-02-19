# Define the strings to be written
lines = ["Hello, world!\n", "Python is fun!\n", "File handling is easy.\n"]

# Open the file in write mode
with open("output.txt", "w") as file:
    # Write each string to the file
    file.writelines(lines)

print("Strings have been written to output.txt")
