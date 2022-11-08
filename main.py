# The enumerate function

friends = ["Rolf", "John", "Anna"]

for counter, friend in enumerate(friends):
  print(counter)
  print(friend)

print(list(enumerate(friends)))

print(list(zip([0, 1, 2], friends)))
  