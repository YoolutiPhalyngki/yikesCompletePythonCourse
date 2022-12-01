"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_maters = defaultdict(list)

for coworker, place in coworkers:
  alma_maters[coworker].append(place)

print(alma_maters)
print(alma_maters['Rolf'][1])
print(alma_maters['Anne'])

alma_maters.default_factory = None

print(alma_maters['Rolf'])
print(alma_maters['Anne'])
print(alma_maters['Jose'])