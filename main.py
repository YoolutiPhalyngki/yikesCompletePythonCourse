class Person:
  def __init__(self, name):
    self.name = name

  @staticmethod
  def greet_friend(friend_name):
    return f'Hey there, {friend_name}'

print(Person.greet_friend('Mike'))