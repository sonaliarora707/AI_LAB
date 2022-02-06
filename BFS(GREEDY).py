from queue import PriorityQueue

vertex = 14
QGraph = [[] for i in range(vertex)]


def Greedy_BFS(src, target, n):
	node_visited = [0] * n
	node_visited[0] = True
	p_queue = PriorityQueue()
	p_queue.put((0, src))
	print("\nSolution to the Graph: \n")
	while p_queue.empty() == False:
		u = p_queue.get()[1]

		print(u, end=" ")
		if u == target:
			break

		for vertex, c in QGraph[u]:
			if (node_visited[vertex] == 0):
				node_visited[vertex] = 1
				p_queue.put((c, vertex))
	print()
 
def Edge(x, y, cost):
	QGraph[x].append((y, cost))
	QGraph[y].append((x, cost))


# The nodes are implemented using integers Edge(x,y,cost);
Edge(0, 1, 3)
Edge(0, 2, 6)
Edge(0, 3, 5)
Edge(1, 4, 9)
Edge(1, 5, 8)
Edge(2, 6, 12)
Edge(2, 7, 14)
Edge(3, 8, 7)
Edge(8, 9, 5)
Edge(8, 10, 6)
Edge(9, 11, 1)
Edge(9, 12, 10)
Edge(9, 13, 2)

src = 0
target = 9
Greedy_BFS(src, target, vertex)