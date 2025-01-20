def sum_of_digits(number):
    # Ensure the number is positive
    number = abs(number)

    # Convert the number to a string, iterate through its digits, and sum them
    return sum(int(digit) for digit in str(number))


# Input from the user
num = int(input("Enter a number: "))

# Calculate and display the sum of digits
print(f"The sum of the digits of {num} is: {sum_of_digits(num)}")