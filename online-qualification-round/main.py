import os
import sys
import math
# from random import perm
import random
import itertools
from files import read_input, parse_input, write_output


def main(args):
    # if len(args) != 1:
    #     print('One argument expected: id of problem to solve (a, b, c, ...)')
    #     sys.exit(-1)

    problem = args[0]

    lines = read_input(problem)

    dur, n_intersections, n_streets, n_cars, n_bonus, streets, cars = parse_input(lines)

    # distances = [(id, sum([streets[edge]['time'] for edge in car['path'] ])) for id, car  in enumerate(cars)]
    # distances.sort(key= lambda x: x[1]) 

    street_car_count = {}

    for street_name in streets:
        street_car_count[street_name] = []

    for car in cars:
        for street_name in car['path']:
            street_car_count[street_name].append(car)

    intersections = {}

    for i in range(n_intersections):

        semaphores = []

        streets_total_car_dist = {}

        for street_name in streets:
            if streets[street_name]['int_end'] == i:
                if len(street_car_count[street_name]) != 0:
                    semaphores.append((street_name, math.ceil(len(street_car_count[street_name]) * 0.01))) 

        #             total_car_dist = 0
        #             for car in street_car_count[street_name]:
        #                 dist_to_int = 0

        #                 for rua in car['path']:
        #                     if rua != street_name:
        #                         dist_to_int += streets[rua]['time']
        #                     else:
        #                         break

        #                 dist_to_int += streets[street_name]['time']
        #                 total_car_dist += dist_to_int
                    
        #             streets_total_car_dist[street_name] = total_car_dist

        # dist_sum = 0
        # for street in streets_total_car_dist:
        #     dist_sum += streets_total_car_dist[street]

        # for j, sem in enumerate(semaphores):

        #     if dist_sum != 0:
        #         semaphores[j] = (sem[0],math.ceil(sem[1] * (2 + streets_total_car_dist[street]/dist_sum)))
        
        if semaphores:
            intersections[i] = random.shuffle(semaphores)

    write_output(problem, intersections)

if __name__ == '__main__':
    main(sys.argv[1:])
