#Scenario 3: Handling Invalid Dictionary Key
try:
    data = {"name": "Alice", "age": 30}
    key = input("Enter the key you want to access: ")
    value = data[key]
    print(f"The value for '{key}' is: {value}")
except KeyError:
    print("Error: The specified key does not exist in the dictionary.")
finally:
    print("Dictionary operation completed.")