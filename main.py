import re

price = 'Price: $18649.50'
expression = 'Price: \$([0-9]*\.[0-9]*)'

matches = re.search(expression, price)
print(matches.group(0))  # entire match
print(matches.group(1))  # first thing in brackets
