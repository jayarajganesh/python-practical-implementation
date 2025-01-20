#factorial using recursive function
def factorial(number):

    if number == 0 or number ==1:
        return 1
    else:
        return number * factorial(number - 1)

number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of the given number {number} is {factorial(number)}")