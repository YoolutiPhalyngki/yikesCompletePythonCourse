"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)

o.move_to_end('Rolf')
o.move_to_end('Jen', last=False)

print(o)

