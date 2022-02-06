QGraph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited_node = set() #To keep track of visited nodes of Graph.

def Depth_First_Search(visited_node, QGraph, node):  # Function for Depth First Search 
    if node not in visited_node:
        print(node,end=" ")
        visited_node.add(node)
        for neighbour in QGraph[node]: # recursion
            Depth_First_Search(visited_node, QGraph, neighbour)

# Driver Code
print("Depth-First Search Output: ",end=" ")
Depth_First_Search(visited_node, QGraph, '5')