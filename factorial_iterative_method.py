
def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

number = int(input("Enter a number to find the factorial: "))
print(f"The factorial of the given number {number} is {factorial(number)}")