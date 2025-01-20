#Scenario 2: File Handling with Non-existent File
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The specified file does not exist.")
except PermissionError:
    print("Error: You do not have permission to read the file.")
finally:
    print("File operation completed.")