# sample_module.py

def greet(name):
    """Greets the user with their name."""
    return f"Hello, {name}!"

def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts the second number from the first."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """Divides the first number by the second."""
    if b == 0:
        return "Error: Division by zero!"
    return a / b