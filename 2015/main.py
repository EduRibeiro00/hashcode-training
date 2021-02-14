from parser import parse_input
from algs.hill_climbing import hill_climbing

if __name__ == "__main__":
    state = parse_input('input/input.txt')
    state.genInitialSolution()
    state.print()

    NUM_ITS = 10

    ####################
    # Hill Climbing
    ####################

    state = hill_climbing(state, NUM_ITS)
    state.print()
