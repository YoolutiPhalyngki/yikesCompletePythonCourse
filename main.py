# Learning default parameters

def add(x, y=3):
  total = x + y
  return total

print(add(5, 10))
print(add(5))
print(add(x=3))
