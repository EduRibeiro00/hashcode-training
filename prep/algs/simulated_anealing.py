from ..state import State
from random import random
import math

def default_temperature_function(current_temperature, _current_iteration, _max_iterations) -> float:
  return max(0, current_temperature - 0.01)

def anealing(init_state: State, num_its: int, temperature_function : function = default_temperature_function, initial_temp: float = 90):
    state = init_state
    temperature = initial_temp

    for i in range(num_its):
      temperature = temperature_function(temperature, i, num_its)

      if temperature < 0.0001:
        return state

      neighbour = next(state.get_all_neighbours(generator=True))

      delta = neighbour.get_value() - state.get_value()

      if delta > 0:
        state = neighbour
      else:
        if random.uniform(0, 1) < math.exp(-delta / temperature):
          state = neighbour


    return state