import re

price = 'Price: $189.50'
expression = 'Price: \$(189.50)'

matches = re.search(expression, price)
print(matches.group(0))
print(matches.group(1))
