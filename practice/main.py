from files.input import parse_input
from files.output import output_to_filename
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Specify the input file in the arguments")
        sys.exit(-1)
    
    state = parse_input(sys.argv[1])
    output_to_filename(state, 'o.txt')