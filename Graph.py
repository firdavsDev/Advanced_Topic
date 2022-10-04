"""
    GRAPH are used to represent many real-life applications like networks, transportation path of city, and social network connections.

    A Graph is set of connected "nodes" where each "NODE" is called a "VERTEX" and  the connection between two of them is called "EDGE"

    For exmaple:
        Connections on social network.
        Each "VERTEX" is a person
        the Edges represent connections
"""

class Graph:
    def __init__(self, size) -> None:
        self.adj = [ [0] * size for _ in range(size)] # [0, 0, ... range(size)] [rangr(size)]
        self.size = size

    def add_edge(self, orig, dest):
        if any([orig > self.size, dest > self.size, orig < 0,  dest < 0]):
            print('Invalid Edge')
        else:
            self.adj[orig-1][dest-1] = 1
            self.adj[dest-1][orig-1] = 1
    
    def remove_edge(self, orig, dest):
        if any([orig > self.size, dest > self.size, orig < 0,  dest < 0]):
            print('Invalid Edge')
        else:
            self.adj[orig-1][dest-1] = 0
            self.adj[dest-1][orig-1] = 0

    def display(self):
        for row in self.adj:
            print(row)
            # for val in row:
            #     print('{:4}'.format(val), end="")

G = Graph(4)
#add
print('------------add------------')
G.add_edge(1,4)
G.add_edge(2,4)
G.add_edge(3,4)
G.add_edge(4,4)
G.display()
#remove
print('------------remove------------')
G.remove_edge(4,4)
G.display()

