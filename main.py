from typing import Callable


def greet():
  print('Hello')


def before_and_after(func: Callable):
  print("Before...")
  func()
  print("After...")


before_and_after(greet)