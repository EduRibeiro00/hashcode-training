from state.state import State


def parse_input(filename):
    """Read input from filename."""
    with open(filename, 'r') as f:
        # create state while extracting first line
        state = State(*[int(x) for x in next(f).split()])

        # save info in state
        for _ in range(state.a):
            x, y, z = [int(i) for i in next(f).split()]
            state.a_values.append((x, y, z))

        for _ in range(state.b):
            x, y = [int(i) for i in next(f).split()]
            state.b_values.append((x, y))

        return state
