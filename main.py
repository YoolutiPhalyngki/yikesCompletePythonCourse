friends = [
  {
    'name': 'Rolf',
    'location': 'Washington, D.C.'
  },
  {
    'name': 'Anna',
    'location': 'San Francisco'
  },
  {
    'name': 'Charlie',
    'location': 'San Francisco'
  },
  {
    'name': 'Jose',
    'location': 'San Francisco'
  }
]

your_location = input('Where are you right now? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if len(friends_nearby) > 0:
  print('You are not alone!')


