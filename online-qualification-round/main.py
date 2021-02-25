import os
import sys
from .files import read_input, parse_input, write_output


def main(args):
    if len(args) != 1:
        print('One argument expected: id of problem to solve (a, b, c, ...)')
        sys.exit(-1)

    problem = args[0]

    read_input(problem)

    parse_input(input)



    write_output(problem)

if __name__ == '__main__':
    main(sys.argv[1:])
