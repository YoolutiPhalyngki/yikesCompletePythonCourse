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

alma_maters.default_factory = int

print(alma_maters['Rolf'])
print(alma_maters['Anne'])
print(alma_maters['Jose'])