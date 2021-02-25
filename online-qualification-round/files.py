import os

def read_input(problem):
    in_path = os.path.join(os.path.dirname(__file__), 'input', f'{problem}.txt')

    with open(in_path) as f:
        input = f.readlines()

    return input

def parse_input(input):




    pass


def write_output(problem):
    out_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f'{problem}.out')

    with open(out_path, 'w') as out:
        # TODO: write output
        out.write('hi')
        pass
