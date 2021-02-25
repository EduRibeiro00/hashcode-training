import os

def read_input(problem):
    in_path = os.path.join(os.path.dirname(__file__), 'input', f'{problem}.txt')

    with open(in_path) as f:
        lines = f.readlines()

    return lines

def parse_input(lines):
    dur, n_intersections, n_streets, n_cars, n_bonus = [int(n) for n in lines[0].split(' ')]

    streets = {}
    for line in lines[1:n_streets+1]:
        int_start, int_end, name, time = [e for e in line.split(' ')]
        street = {
            'int_start': int(int_start),
            'int_end': int(int_end),
            'time': int(time),
            'name': name
        }

        streets[name] =street

    cars = []
    for line in lines[1+n_streets:]:
        split_line = line.split(' ')
        car = {
            'n_streets': int(split_line[0]),
            'path': split_line[1:-1]
        }
        cars.append(car)

    return dur, n_intersections, n_streets, n_cars, n_bonus, streets, cars


def write_output(problem):
    out_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f'{problem}.out')

    with open(out_path, 'w') as out:
        # TODO: write output
        pass
