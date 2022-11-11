# Learning Magic methods in Python

class Student:
  def __init__(self, name):
    self.name = name

movies = ['Matrix', 'Finding Nemo']


class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def __getitem__(self, i):
    return self.cars[i]

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(len(ford))
print(ford[0]) # Garage.__getitem__(ford, 0)


