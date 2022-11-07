# Set and dictionary comprehension

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "micheal"]

friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

print(friends_lower.intersection(guests_lower))
