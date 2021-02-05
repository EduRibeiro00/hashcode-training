def parse_input(filename):
    with open(filename, 'r') as f:
        # extract first line
        num_rows, num_slots, num_unavailable_slots, num_pools, num_servers = [int(x) for x in next(f).split()]

        # create data center matrix (True means empty slot)
        rows = [[True]*num_slots]*num_rows

        # mark unavailable slots
        for _ in range(num_unavailable_slots):
            y, x = [int(x) for x in next(f).split()]
            rows[x][y] = False

        servers = []

        # parse servers
        for _ in range(num_servers):
            size, capacity = [int(x) for x in next(f).split()]
            servers.append({'size': size, 'capacity': capacity})

        print('*'*100)
        print('Data center:')
        for row in rows:
            print(row)
        print('*'*100)
        print('Servers:')
        for server in servers:
            print(server)
        print('*'*100)
        print('Num pools:')
        print(num_pools)
        print('*'*100)