friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(lambda friend: friend.startswith('R'), friends)

another_starts_with_r = (f for f in friends if f.startswith('R'))

friends_lower = map(lambda x: x.lower(), friends)
friends_lower = [friend.lower() for friend in friends]
friends_lower = (friend.lower() for friend in friends)

print(next(friends_lower))
