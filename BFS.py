# BFS implementation using Python 
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited_nodes = [] # List for visited nodes nodes.
queue = []   # Initialize a queue

def breadth_first_search(visited_nodes, graph, node): # function for BFS
  visited_nodes.append(node)
  queue.append(node)

  while queue:          # to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited_nodes:
        visited_nodes.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Output for Breadth-First Search")
breadth_first_search(visited_nodes, graph, '5')    # function calling