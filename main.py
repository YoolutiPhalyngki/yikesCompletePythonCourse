def starts_with_r(friend):
  return friend.startswith('R')

friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(starts_with_r, friends)

print(next(start_with_r))
print(next(start_with_r))
print(next(start_with_r))