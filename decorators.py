#Example 1: Logging Decorator
# Define the decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)  # Call the original function
        print(f"Finished function: {func.__name__}")
        return result
    return wrapper

# Use the decorator
@log_decorator
def greet(name):
    print(f"Hello, {name}!")

# Call the decorated function
greet("Alice")

#Example 2: Timing Decorator
import time

# Define the decorator
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Use the decorator
@timing_decorator
def slow_function():
    time.sleep(2)  # Simulate a slow task
    print("Finished slow task!")

# Call the decorated function
slow_function()