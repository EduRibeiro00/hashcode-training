from files.input import parse_input
from files.output import output_to_filename
from state.pizza import PizzaAllocation
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Specify the input file in the arguments")
        sys.exit(-1)
    
    state = parse_input(sys.argv[1])
    state.print()

    teams_with_pizzas = 0

    for _ in range(state.num_teams_4):
        pizzas_for_team = PizzaAllocation()
        inserted_one = False
        if len(state.pizzas) < 4:
            break
        for _ in range(4):
            inserted = pizzas_for_team.add_pizza(state.select_pizza_for_team(pizzas_for_team))
            if inserted:
                inserted_one = True
        if inserted_one:
            teams_with_pizzas += 1
        state.pizza_allocation['4'].append(pizzas_for_team)

    for _ in range(state.num_teams_3):
        pizzas_for_team = PizzaAllocation()
        inserted_one = False
        if len(state.pizzas) < 3:
            break
        for _ in range(3):
            inserted = pizzas_for_team.add_pizza(state.select_pizza_for_team(pizzas_for_team))
            if inserted:
                inserted_one = True
        if inserted_one:
            teams_with_pizzas += 1
        state.pizza_allocation['3'].append(pizzas_for_team)

    for _ in range(state.num_teams_2):
        pizzas_for_team = PizzaAllocation()
        inserted_one = False
        if len(state.pizzas) < 2    :
            break
        for _ in range(2):
            inserted = pizzas_for_team.add_pizza(state.select_pizza_for_team(pizzas_for_team))
            if inserted:
                inserted_one = True
        if inserted_one:
            teams_with_pizzas += 1
        state.pizza_allocation['2'].append(pizzas_for_team)

    output_to_filename(state, teams_with_pizzas, 'o.txt')