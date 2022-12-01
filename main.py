"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_maters = {}

for coworker in coworkers:
  if coworker[0] not in alma_maters:
    alma_maters[coworker[0]] = []
  alma_maters[coworker[0]].append(coworker[1])

print(alma_maters)
