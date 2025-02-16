# Open the file in write mode (creates if it doesn't exist)
with open("myfile.txt", "w") as file:
    # Write a string to the file
    file.write("Hello, this is a sample text written to the file.")

print("File has been created and the string has been written successfully.")
