
class State(object):

  def __init__(self) -> None:
    self.value = None

  def calc_random_solution(self):
    """Calculates a random solution for the problem."""
    pass

  def get_all_neighbours(self, generator=True) -> list('State'):
    """Generates all neighbors of the current state."""
    return []

  def get_random_neighbour(self) -> 'State':
    """Generates a random neighbor."""
    return None

  def get_value(self) -> float:
    """Gets the value of the current state."""
    if self.value is None:
      self.value = self.calc_value()

    return self.value

  def calc_value(self):
    """Calculates the value for the current state."""
    return 0

  def __str__(self):
    return "state"

  def __eq__(self, o: 'State') -> bool:
      return self.get_value() == o.get_value()

  def __lt__(self, o: 'State') -> bool:
      return self.get_value() < o.get_value()
