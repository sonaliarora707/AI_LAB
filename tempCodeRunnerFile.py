# A * algorithm implementation using Python and Package "queue"

from collections import deque

class QuesGraph:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n): # heuristic 
        H = {
            'S': 14,
            'B': 12,
            'C': 11,
            'D': 6,
            'E': 4,
            'F': 11,
            'G': 0
        }

        return H[n]

    def A_Star_Algo(self, first, stop):

        open = set([first])
        closed = set([])

        g = {}

        g[first] = 0

        parent = {}
        parent[first] = first

        while len(open) > 0:
            n = None

            for v in open:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print('Non Existent Path!')
                return None


            if n == stop:
                new_path = []

                while parent[n] != n:
                    new_path.append(n)
                    n = parent[n]

                new_path.append(first)

                new_path.reverse()

                print('\nPath found:\n {}'.format(new_path),"\n")
                return new_path

            for (m, weight) in self.get_neighbors(n):

                if m not in open and m not in closed:
                    open.add(m)
                    parent[m] = n
                    g[m] = g[n] + weight


                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parent[m] = n

                        if m in closed:
                            closed.remove(m)
                            open.add(m)

            open.remove(n)
            closed.add(n)

        print('Path does not exist!')
        return None
    
# Driver code with the example from the notes slide
adjacency_list = {
    'S': [('B', 4), ('C', 3)],
    'B': [('E', 12),('F',5)],
    'C': [('E', 10),('D',7)],
    'D': [('E', 2)],
    'E': [('G', 5)],
    'F': [('G', 16)]
}
graph1 = QuesGraph(adjacency_list)
graph1.A_Star_Algo('S', 'G')