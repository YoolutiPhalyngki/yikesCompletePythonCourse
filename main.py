# Problem on lists, set
lottery_numbers = {13, 21, 22, 5, 8}

players = [
  {
    'name': "Joe",
    'number': {1, 7, 88, 8}
  }, 
  {
    'name': "Mac",
    'number': { 2, 21, 3, 31, 8, 77, 5}
  }
]

player1_count = len(players[0]['number'].intersection(lottery_numbers))

player2_count = len(players[1]['number'].intersection(lottery_numbers))

print(players[0]['name'],player1_count)
print(players[1]['name'],player2_count)

print(f"Player {players[0]['name']} got {player1_count} numbers right")

print(f"Player {players[1]['name']} got {player2_count} numbers right")