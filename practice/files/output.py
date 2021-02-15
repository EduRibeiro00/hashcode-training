# -*- coding: utf-8 -*-
def output_to_filename(state, num_total_pizzas, filename):
    """Outputs the state information to the filename."""
    f = open(filename, 'w')
    f.write('{}\n'.format(num_total_pizzas))
    for allocation in state.pizza_allocation['2']:
        if len(allocation.pizzas_for_team) < 1:
            continue

        f.write('2')
        for pizza in allocation.pizzas_for_team:
            f.write(' {}'.format(pizza.index))
        f.write('\n')

    for allocation in state.pizza_allocation['3']:
        if len(allocation.pizzas_for_team) < 1:
            continue

        f.write('3')
        for pizza in allocation.pizzas_for_team:
            f.write(' {}'.format(pizza.index))
        f.write('\n')

    for allocation in state.pizza_allocation['4']:
        if len(allocation.pizzas_for_team) < 1:
            continue

        f.write('4')
        for pizza in allocation.pizzas_for_team:
            f.write(' {}'.format(pizza.index))
        f.write('\n')

    f.close()
