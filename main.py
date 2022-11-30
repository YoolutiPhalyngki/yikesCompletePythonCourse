age = 20

def increase_age(current_age):
  current_age = current_age + 1

print(id(age))
increase_age(age)
print(id(age))
