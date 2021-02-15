from .state import State
from .algs import *


class ClassState(State):
  def __init__(self, state) -> None:
    self.state = state
  
  # def get_all_neighbours(self, generator = True) -> list('State'):

  #   result = []

  #   for student in self.state:



  #   if not generator:
  #     return result

  def get_value(self) -> float:
    return 0

  def display(self) -> None:
    print('Empty state {}, nothing to display.'.format(id(self)))

  def __eq__(self, o: 'State') -> bool:
      return self.get_value() == o.get_value()

  def __lt__(self, o: 'State') -> bool:
      return self.get_value() < o.get_value()
