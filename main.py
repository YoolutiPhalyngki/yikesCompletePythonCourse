# Learning Lambda functions in Python

average = lambda sequence: sum(sequence) / len(sequence)

students = [
  {"name": "Rolf", "grades": (67, 90, 95, 100)},
  {"name": "Bob", "grades": (56, 78, 80, 90)},
  {"name": "Jen", "grades": (98, 90, 95, 99)},
  {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
  print(average(student["grades"]))

