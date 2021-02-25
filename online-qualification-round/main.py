import os
import sys
from files import read_input, parse_input, write_output


def main(args):
    if len(args) != 1:
        print('One argument expected: id of problem to solve (a, b, c, ...)')
        sys.exit(-1)

    problem = args[0]

    lines = read_input(problem)

    dur, n_intersections, n_streets, n_cars, n_bonus, streets, cars = parse_input(lines)

    # distances = [(id, sum([streets[edge]['time'] for edge in car['path'] ])) for id, car  in enumerate(cars)]
    # distances.sort(key= lambda x: x[1]) 

    street_car_count = {}

    for street_name in streets:
        street_car_count[street_name] = 0

    for car in cars:
        for street_name in car['path']:
            street_car_count[street_name] += 1

    intersections = {}

    for i in range(n_intersections):

        semaphores = []

        for street_name in streets:
            if streets[street_name]['int_end'] == i:
                if street_car_count[street_name] != 0:
                    semaphores.append((street_name, street_car_count[street_name])) 

        if semaphores:
            intersections[i] = semaphores

    write_output(problem, intersections)

if __name__ == '__main__':
    main(sys.argv[1:])
