def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Add:", add(a, b))
print("Sub:", sub(a, b))
print("Mul:", mul(a, b))
print("Div:", div(a, b))