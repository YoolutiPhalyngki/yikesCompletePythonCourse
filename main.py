from typing import Callable


def greet():
  print('Hello')


def before_and_after(func: Callable):
  print("Before...")
  print(func())
  print("After...")


before_and_after(greet())