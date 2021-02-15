
class State(object):

  def __init__(self) -> None:
    pass

  def get_all_neighbours(self, generator=True) -> list('State'):
    return []

  def get_value(self) -> float:
    return 0

  def display(self) -> None:
    print('Empty state {}, nothing to display.'.format(id(self)))

  def __eq__(self, o: 'State') -> bool:
      return self.get_value() == o.get_value()

  def __lt__(self, o: 'State') -> bool:
      return self.get_value() < o.get_value()
