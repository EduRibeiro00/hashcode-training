import os

def read_input(problem):
    in_path = os.path.join(os.path.dirname(__file__), 'input', '{}.txt'.format(problem))

    with open(in_path) as f:
        lines = f.readlines()

    return lines

def parse_input(lines):
    dur, n_intersections, n_streets, n_cars, n_bonus = [int(n) for n in lines[0].split(' ')]

    streets = []
    for line in lines[1:n_streets+1]:
        int_start, int_end, name, time = [e for e in line.split(' ')]
        street = {
            'int_start': int(int_start),
            'int_end': int(int_end),
            'name': name,
            'time': int(time)
        }
        streets.append(street)

    cars = []
    for line in lines[1+n_streets:]:
        split_line = line.split(' ')
        car = {
            'n_streets': int(split_line[0]),
            'path': split_line[1:]
        }
        cars.append(car)

    return dur, n_intersections, n_streets, n_cars, n_bonus, streets, cars


def write_output(problem, intersections):
    out_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, '{}.out'.format(problem))

    with open(out_path, 'w') as out:
        out.write(str(len(intersections)) + '\n')

        for id, v in intersections.items():
            out.write(str(id) + '\n')
            out.write(str(len(v)) + '\n')
            for s, d in v:
                out.write('{} {}\n'.format(s, d))

