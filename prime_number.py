# Function to check if a number is prime
def is_prime(num):
    if num <= 1:  # Numbers less than or equal to 1 are not prime
        return False

    # Check divisors from 2 to sqrt(num) for efficiency
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If divisible by any number, not a prime
            return False

    return True


# Input: Number to check
number = int(input("Enter a number to check if it's prime: "))

# Check and display result
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")