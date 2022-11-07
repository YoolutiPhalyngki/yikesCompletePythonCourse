# List comprehension with conditions

ages = [22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]

print(odds)
