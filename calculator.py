def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    return "Cannot divide with zero!"
  else:
    return a / b

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

print("Sum: ", add(num1, num2))
print("Difference: ", subtract(num1, num2))
print("Product: ", multiply(num1, num2))
print("Quotient: ", divide(num1, num2))1
