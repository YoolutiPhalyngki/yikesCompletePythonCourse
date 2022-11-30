accounts = {
  'checking': 1958.00,
  'savings': 3695.50
}

def add_balance(amount: float, name: str) -> float:
  """Function to update the balance of an account and return the new balance."""
  accounts[name] += amount
  return accounts[name]


transactions = [
  (-180.67, 'checking'),
  (-220.00, 'checking'),
  (220.00, 'savings'),
  (-15.70, 'checking'),
  (-23.90, 'checking'),
  (-13.00, 'checking'),
  (1579.50, 'checking'),
  (-600.50, 'checking'),
  (600.50, 'savings'),
]

for t in transactions:
  add_balance(name=t[1], amount=t[0])



class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password


# imagine these users are coming from a database...
users = [
  {'username': 'rolf', 'password': '123'},
  {'username': 'tecladoisawesome', 'password': 'youaretoo'}
]

user_objects = [User(data['username'], data['password']) for data in users]
user_objects = [User(username=data['username'], password=data['password']) for data in users]
user_objects = [User(**data) for data in users]

print(user_objects)

users = [
  ('rolf', '123'),
  ('tecladoisawesome', 'youaretoo')
]

user_objects = [User(*data) for data in users]

print(user_objects)
