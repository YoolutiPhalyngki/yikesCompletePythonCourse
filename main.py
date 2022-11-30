primes = [2, 3, 5]

print(id(primes))

primes += [7, 11]  # primes = primes.__iadd__([7, 11])

print(id(primes))
