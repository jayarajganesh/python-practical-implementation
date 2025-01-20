def is_armstrong(number):
    # Convert the number to a string to get the digits
    digits = str(number)
    # Find the number of digits (the power)
    num_digits = len(digits)
    # Calculate the sum of digits raised to the power of num_digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    # Check if the sum equals the original number
    return armstrong_sum == number

# Input from the user
num = int(input("Enter a number to check if it is an Armstrong number: "))

# Check and display the result
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")