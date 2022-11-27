friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(lambda friend: friend.startswith('R'), friends)

another_starts_with_r = (f for f in friends if f.startswith('R'))

print(list(another_starts_with_r))
print(list(another_starts_with_r))
