import re

email = 'jose@tecladocode.com'
expression = '[a-z\.]+'

matches = re.findall(expression, email)
print(matches)

name = matches[0]
domain = matches[1]

print(name)
print(domain)

