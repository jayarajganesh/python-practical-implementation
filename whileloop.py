#1. Basic Counter
counter = 0
while counter < 5:
    print(counter)
    counter += 1

#2. Sum of Numbers
num = 1
total = 0
while num <= 10:
    total += num
    num += 1
print(f"Sum: {total}")

#3. User Input Validation
num = -1
while num < 0:
    num = int(input("Enter a positive number: "))
print(f"You entered: {num}")


#4. Infinite Loop with Break
count = 0
while True:
    print("Looping...")
    count += 1
    if count == 3:
        break