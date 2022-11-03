# Learning while loop

user_input = input("Do you want to print? (p/q): ")

while not(user_input == "q"):
  if user_input == "p":
    print("Hello")
  user_input = input("Do you want to print? (p/q): ")

print("We stopped running.")
  