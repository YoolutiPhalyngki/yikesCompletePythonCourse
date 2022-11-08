# The enumerate function

friends = ["Rolf", "John", "Anna"]

temp = list(enumerate(friends))
#temp = list(zip([0, 1, 2], friends))

for counter, friend in temp:
  print(counter)
  print(friend)


  