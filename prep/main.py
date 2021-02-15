from files.input import parse_input
from files.output import output_to_filename


if __name__ == '__main__':
    state = parse_input('i.txt')
    output_to_filename(state, 'o.txt')