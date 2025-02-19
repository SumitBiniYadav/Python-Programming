# Define the string to be written
text = "Hello, this is a sample text written to a file."

# Open the file in write mode
with open("output.txt", "w") as file:
    # Write the string to the file
    file.write(text)

print("File 'output.txt' has been created and text has been written.")
