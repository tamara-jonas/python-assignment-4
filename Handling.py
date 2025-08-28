filename = input("Enter the filename to read: \n")

try:
    with open(filename, "r") as file:
        content = file.read()
    with open("modified_" + filename, "w") as new_file:
        new_file.write(content.upper())
    print("Modified file created as:", "modified_" + filename)
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Cannot read the file.")