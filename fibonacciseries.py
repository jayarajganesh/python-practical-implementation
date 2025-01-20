def fibonacci_while(n):
    num1 = 0
    num2 = 1
    next_number = num2
    result = []
    count = 0

    while count < n:

        result.append(num1)
        num1, num2 = num2, next_number
        next_number = num1 + num2
        count += 1

    return result


# Input from the user
num = int(input("Enter the number of terms in the Fibonacci series: "))

# Generate and display the Fibonacci series
print(f"The first {num} terms of the Fibonacci series are: {fibonacci_while(num)}")