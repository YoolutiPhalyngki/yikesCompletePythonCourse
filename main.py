"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

from collections import namedtuple

account = ('checking', 1850.90)

Account = namedtuple('Account', ['name', 'balance'])

accountNamedTuple = Account._make(account)

print(accountNamedTuple)

