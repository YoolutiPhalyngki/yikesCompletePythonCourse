# Learning else with loop

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]
all_successful = True

for status in cars:
  if status == "faulty":
    print("Stopping the production line!")
    all_successful = False
    break
  print(f"This car is {status}.")
  print("Shipping new cat to customer!")

if all_successful:
  print("All cars built successfully. No faulty cars!")