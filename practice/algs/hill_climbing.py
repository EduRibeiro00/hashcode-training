from ..state import State

def hill_climbing(init_state: State, num_its: int):
    """Regular hill climbing algorithm."""
    state = init_state

    for _ in range(num_its):
        # create generator that yields all state neighbors
        old_state = state
        neighbours = state.get_all_neighbours(generator=True)
        for neighbour in neighbours:
            # new best neighbor
            if state < neighbour:
                state = neighbour
                break

        # state was not updated, return
        if old_state == state:
            return state

    return state


def steepest_ascent(init_state: State, num_its: int):
    """HC that gets the best neighbor."""
    state = init_state

    for _ in range(num_its):
        # create generator that yields all state neighbors
        neighbours = state.get_all_neighbours(generator=False)
        best_neighbour = max(neighbours)

        if state <= best_neighbour:
            state = best_neighbour

    return state


def stochastic_hill_climbing(init_state: State, max_tries: int):
    """Gets random neighbor each time."""
    num_tries = 0
    state = init_state
    while max_tries > num_tries:
        random_neighbor = state.get_random_neighbour()
        if random_neighbor.get_value() > state.get_value():
            state = random_neighbor
            num_tries = 0
        else:
            num_tries += 1

        if num_tries < max_tries:
            break

    return state


def random_restart(init_state: State, max_tries: int, rr_its: int):
    """Start again in a new position after a while.
    Good for when there are a lot of local maxs/mins."""
    num_tries = 0
    state = init_state
    while rr_its > num_tries:
        random_neighbor = state.get_random_neighbour()
        if random_neighbor.get_value() > state.get_value():
            state = random_neighbor
            num_tries = 0
        else:
            num_tries += 1

        if num_tries < max_tries:
            state.calc_random_solution()
            num_tries = 0

    return state