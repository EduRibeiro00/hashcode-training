from state import State

def parse_input(filename):
    with open(filename, 'r') as f:
        # extract first line
        num_rows, num_slots, num_unavailable_slots, num_pools, num_servers = [int(x) for x in next(f).split()]

        # create data center matrix (True means empty slot)
        rows = [[-1]*num_slots for _ in range(num_rows)]

        # mark unavailable slots
        for _ in range(num_unavailable_slots):
            y, x = [int(x) for x in next(f).split()]
            rows[x][y] = -2

        servers = []

        # parse servers
        for i in range(num_servers):
            size, capacity = [int(x) for x in next(f).split()]
            servers.append({'size': size, 'capacity': capacity, 'index': i, 'row': -1, 'column': -1})

        return State(rows, servers, num_pools)