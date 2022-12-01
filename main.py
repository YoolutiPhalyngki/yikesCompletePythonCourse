"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

from collections import Counter

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.5])

print(Counter({'hello': 5, 'hi': 3})['hi'])
