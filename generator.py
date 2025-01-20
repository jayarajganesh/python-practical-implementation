#Example 1: Simple Counter Generator
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Give one value at a time
        count += 1

# Use the generator
for number in count_up_to(3):
    print(number)

print("-------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#Example 2: Generator for Even Numbers
def even_numbers(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2

# Use the generator
for even in even_numbers(6):
    print(even)