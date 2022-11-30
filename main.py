friends_last_seen = {
  'Rolf': 31,
  'Jen': 1,
  'Anne': 7
}

print(id(friends_last_seen))

friends_last_seen = {
  'Rolf': 31,
  'Jen': 1,
  'Anne': 7
}

print(id(friends_last_seen))

friends_last_seen['Rolf'] = 0

print(id(friends_last_seen))

my_int = 5

print(id(my_int))

my_int = my_int + 1

print(id(my_int))

friends = ['Rolf', 'Jose']
print(id(friends))

friends.append('Jen')
print(id(friends))

"""
Immutable:
integers
floats
strings
tuples
"""