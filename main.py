# The enumerate function

friends = ["Rolf", "John", "Anna"]

for counter, friend in enumerate(friends):
  print(counter)
  print(friend)

print(enumerate(friends))
print(list(enumerate(friends)))
print(dict(enumerate(friends)))
  