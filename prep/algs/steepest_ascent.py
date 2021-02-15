from ..state import State

def hill_climbing(init_state: State, num_its: int):
    state = init_state

    for _ in range(num_its):
        # create generator that yields all state neighbors
        neighbours = state.get_all_neighbours(generator=False)
        best_neighbour = max(neighbours)

        if state < best_neighbour:
            state = best_neighbour

    return state