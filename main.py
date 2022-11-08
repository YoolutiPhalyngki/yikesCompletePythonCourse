# Exercise: an improved lottery!

import random

lottery_numbers = set(random.sample(list(range(22)), 6))

players = [
  {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
  {"name": "Charlie", "numbers": {2, 7, 9, 22, 10, 5}},
  {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
  {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

top_player = players[0]

for player in players:
  match_number = len(player["numbers"].intersection(lottery_numbers))
  if match_number > len(top_player["numbers"].intersection(lottery_numbers)):
    top_player = player

winner_earning = 100 ** len(top_player["numbers"].intersection(lottery_numbers))
print(f"{top_player['name']} won {winner_earning}.")
