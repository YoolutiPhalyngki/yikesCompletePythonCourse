# The enumerate function

friends = ["Rolf", "John", "Anna"]

for counter, friend in enumerate(friends, start=1):
  print(counter)
  print(friend)

print(enumerate(friends))
print(list(enumerate(friends)))
print(dict(enumerate(friends)))
  