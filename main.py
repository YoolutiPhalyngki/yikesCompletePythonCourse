"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

from collections import deque

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
print(friends)

friends.append('Jose')
friends.appendleft('Anthony')

print(friends)

friends.pop()
friends.popleft()

print(friends)


