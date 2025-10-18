def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def square(x):
    return x * x

def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b

def mod(a, b):
    if b == 0:
        raise ValueError("modulo by zero")
    return a % b

def power(a, b):
    return a ** b

