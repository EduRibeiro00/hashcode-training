import sys
from copy import deepcopy


class State:
    """
    For the rows matrix:
    -2 -> cell is restricted; not occupiable
    -1 -> cell is empty
    x -> cell is occupied by server with index x (x >= 0)

    Each solution will:
    - assign servers to positions (or not)
    - assign servers to pools (if they are assigned to a position)
    """

    def __init__(self, rows, servers, num_pools):
        self.rows = rows
        self.servers = servers
        self.num_pools = num_pools
        self.pool_allocation = None
        self.value = None

    def print(self):
        print('*' * 50)
        print('Data center:')
        for row in self.rows:
            print(row)
        print('*' * 50)
        print('Servers:')
        for server in self.servers:
            print(server)
        print('*' * 50)

        if self.pool_allocation is not None:
            print('Pool allocation:')
            print(self.pool_allocation)

        print("Value of state: {}".format(self.getValue()))

    def getValue(self):
        if self.value is None:
            self.value = self.calcValueForState()
        return self.value

    def genInitialSolution(self):
        # part 1: greedily assign servers to positions
        for server in self.servers:
            inserted = False
            for row_idx, row in enumerate(self.rows):
                if inserted:
                    break

                first_idx = None
                empty_len = 0
                for col_idx, cell in enumerate(row):
                    if cell != -1 or col_idx == len(row) - 1:
                        if col_idx == len(row) - 1 and cell == -1:
                            empty_len += 1
                            first_idx = (row_idx, col_idx) if first_idx is None else first_idx

                        if empty_len >= server['size']:
                            self.insertServerAt(server, first_idx[0], first_idx[1])
                            inserted = True
                            break

                        first_idx = None
                        empty_len = 0

                    else:
                        if first_idx is None:
                            empty_len = 1
                            first_idx = (row_idx, col_idx)
                        else:
                            empty_len += 1

        # part 2: greedily assign servers to pools (every server allocated to pool 0)
        if self.num_pools < 1:
            print("No pools?!")
            return

        self.pool_allocation = [0] * len(self.servers)

    def insertServerAt(self, server, row_idx, col_idx):
        server['row'] = row_idx
        server['column'] = col_idx
        for i in range(server['size']):
            self.rows[row_idx][col_idx + i] = server['index']

    def removeServerAt(self, server, row_idx, col_idx):
        server['row'] = -1
        server['column'] = -1
        for i in range(server['size']):
            self.rows[row_idx][col_idx + i] = -1

    def calcValueForState(self):
        max_guaranteed_cap_all = sys.maxsize
        for pool in range(self.num_pools):
            pool_max_guaranteed_cap = sys.maxsize
            for i in range(len(self.rows)):
                guaranteed_cap = 0
                for server in self.servers:
                    if self.pool_allocation[server['index']] != pool or server['row'] == i:
                        continue
                    guaranteed_cap += server['capacity']

                pool_max_guaranteed_cap = min(pool_max_guaranteed_cap, guaranteed_cap)
            max_guaranteed_cap_all = min(max_guaranteed_cap_all, pool_max_guaranteed_cap)

        return max_guaranteed_cap_all

    def serverWouldFit(self, server, another_server):
        row = another_server['row']
        for i in range(server['size']):
            cur_col = another_server['column'] + i
            if cur_col >= len(self.rows[row]):
                return False
            cell = self.rows[row][cur_col]
            if cell != -1 and cell != another_server['index']:
                return False

        return True

    ####################################
    # generating new states (neighbors)
    ####################################

    def genAllNeighbors(self):
        # option 1: trocar servers de sitio
        for server in self.servers:
            # server is allocated to a row
            if server['row'] != -1:
                for another_server in self.servers:
                    # another server which is allocated to a row
                    if another_server['row'] != -1 and server != another_server:
                        if self.serverWouldFit(server, another_server) and \
                                self.serverWouldFit(another_server, server):
                            yield self.swapServers(server, another_server)

        # option 2: substituir servers
        # TODO

        # option 3: mudar a pool dos servers
        # TODO

    def swapServers(self, server, another_server):
        new_state = deepcopy(self)
        prev_server_row = server['row']
        prev_server_col = server['column']
        new_state.insertServerAt(server, another_server['row'], another_server['column'])
        new_state.insertServerAt(another_server, prev_server_row, prev_server_col)
        return new_state
