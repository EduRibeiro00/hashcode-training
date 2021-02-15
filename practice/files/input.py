from state.state import State
from state.pizza import Pizza

def parse_input(filename):
    """Read input from filename."""

    with open(filename, 'r') as f:
        # create state while extracting first line
        state = State(*[int(x) for x in next(f).split()])

        # save info in state
        for i in range(state.num_pizzas):
            line = next(f).split()
            state.pizzas.append(Pizza(i, int(line[0]), line[1:]))

        return state
