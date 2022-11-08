# The enumerate function

friends = ["Rolf", "John", "Anna"]

counter = 0

for friend in friends:
  print(counter)
  print(friend)
  index = counter + 1


for counter, friend in enumerate(friends):
  print(counter)
  print(friend)
  
  