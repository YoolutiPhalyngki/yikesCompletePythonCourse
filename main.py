# Learning Functions and return values in Python

def divide(x, y):
  if y == 0:
    return "You tried to divide by zero!"
  else:
    return x / y

print(divide(10, 2))
print(divide(6, 0))