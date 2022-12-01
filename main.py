from collections import defaultdict, OrderedDict, namedtuple, deque

def task1() -> defaultdict:
  my_dict = defaultdict(lambda: 'Unknown')
  my_dict['Alan'] = 'Manchester'

  return my_dict

def task2(arg_od: OrderedDict):
  arg_od.popitem()
  arg_od.popitem(last=False)
  arg_od.move_to_end('Bob')
  arg_od.move_to_end('Dan', last=False)

# my_dict = OrderedDict([
#   ('Alan', 'Manchester'),
#   ('Bob', 'London'),
#   ('Chris', 'Lisbon'),
#   ('Dan', 'Paris'),
#   ('Eden', 'Liverpool'),
#   ('Frank', 'Newcastle')
# ])

# task2(my_dict)


def task3(name: str, club: str) -> namedtuple:
  Player = namedtuple('Player',['name', 'club'])
  playerNamedTuple = Player(name, club)
  
  return playerNamedTuple

# player = ('Ronaldo', 'Manchester')

# playerNamedTuple = task3(*player)
# print(playerNamedTuple)


def task4(arg_deque: deque):
  arg_deque.pop()
  arg_deque.append(arg_deque.popleft())
  arg_deque.appendleft('Zack')

# friends = deque(('Rolf', 'Mack', 'Jerry', 'Anna', 'Jose'))

# task4(friends)
