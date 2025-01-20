def sum_of_digits(number):
    total = 0

    # Loop through the digits of the number
    while number > 0:
        total += number % 10  # Get the last digit and add it to the total
        print(total)
        number //= 10  # Remove the last digit

    return total


# Input the number
number = int(input("Enter a number: "))

# Call the function and print the result
print("Sum of digits:", sum_of_digits(number))