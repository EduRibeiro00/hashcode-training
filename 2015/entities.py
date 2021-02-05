class DataCenter:
    def __init__(self, rows):
        self.rows = rows


class Server:
    def __init__(self, size, capacity):
        self.size = size
        self.capacity = capacity


class Pool:
    def __init__(self):
        self.servers = []

    def add_server(self, server):
        self.servers.append(server)