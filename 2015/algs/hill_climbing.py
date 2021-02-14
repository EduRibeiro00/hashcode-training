from state import State

def hill_climbing(init_state, num_its):
    state = init_state
    best_value = state.getValue()

    for _ in range(num_its):
        # create generator that yields all state neighbors
        neighbours = state.genAllNeighbors()
        for neighbour in neighbours:
            # new best neighbor
            if best_value < neighbour.getValue():
                best_value = neighbour.getValue()
                state = neighbour

    return state