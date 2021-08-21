from collections import defaultdict

"""
# Credit for https://www.geeksforgeeks.org/detect-cycle-undirected-graph/ 
    for the GraphClass and cycle function
    
    
    In this question I needed to build a Python Program to detect cycle in an undirected graph.
    
    I have created a graph class with a few functions:
        Ctor, addEdge, isCyclicUtils, isCyclic
        
        addEdge takes two vertices and creates an edge from them.
        
        isCyclicUtils is a recursive function that uses a visited array            
        If an adjacent vertex is visited and not parent of current vertex, then there is a cycle
        
        isCyclic runs on every vertex and calls isCyclicUtils
    
    I am creating a graph, and adding edges to it.
    once I'm done the graph will be send to isCyclic
    
"""



def func():
    n, m = [int(n) for n in input().split()]
    graphArray = [int(n) for n in input().split()]

    if n < m:
        return 1

    graph = Graph(n)

    i = 0
    while i in range(2 * m):
        graph.addEdge(graphArray[i], graphArray[i + 1])
        i += 2

    if graph.isCyclic() == True:
        return 1
    else:
        return 0


# This class represents a undirected
# graph using adjacency list representation
class Graph:

    def __init__(self, vertices):

        # No. of vertices
        self.V = vertices  # No. of vertices

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, v, w):

        # Add w to v_s list
        self.graph[v].append(w)

        # Add v to w_s list
        self.graph[w].append(v)

    # A recursive function that uses
    # visited[] and parent to detect
    # cycle in subgraph reachable from vertex v.
    def isCyclicUtil(self, v, visited, parent):

        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.graph[v]:

            # If the node is not
            # visited then recurse on it
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, v)):
                    return True
            # If an adjacent vertex is
            # visited and not parent
            # of current vertex,
            # then there is a cycle
            elif parent != i:
                return True

        return False

    # Returns true if the graph
    # contains a cycle, else false.
    def isCyclic(self):

        # Mark all the vertices
        # as not visited
        visited = [False] * (self.V)

        # Call the recursive helper
        # function to detect cycle in different
        # DFS trees
        for i in range(self.V):

            # Don't recur for u if it
            # is already visited
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, -1)) == True:
                    return True

        return False


t = int(input())
for i in range(t):
    print(func())
