# List comprehension in Python

friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
  print(f"{friend.title()} is one of your friends.")
