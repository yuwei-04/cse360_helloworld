def add(a, b):
    """Return a + b."""
    return a + b

def subtract(a, b):
    """Return a - b."""
    return a - b

def mul(a, b):
    """Return a * b."""
    return a * b

def square(x):
    """Return x * x."""
    return x * x

def divide(a, b):
    """Return a / b. Raise ValueError on division by zero."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b

def mod(a, b):
    """Return a % b. Raise ValueError on modulo by zero."""
    if b == 0:
        raise ValueError("modulo by zero")
    return a % b

def power(a, b):
    """Return a ** b (integer/float power)."""
    return a ** b

