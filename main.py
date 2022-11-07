# Set and dictionary comprehension

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "micheal"]

friends_lower = {n.title() for n in friends}
guests_lower = {n.title() for n in guests}

present_friends = friends_lower.intersection(guests_lower)

print(present_friends)
