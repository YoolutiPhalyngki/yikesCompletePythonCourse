import re

price = 'Price: $189.50'
expression = 'Price: \$(189.50)'

matches = re.search(expression, price)
print(matches.group(0))  # entire match
print(matches.group(1))  # first thing in brackets
