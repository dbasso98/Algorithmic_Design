class Node:
    """
    A node has the following characteristics:
        • the index of the node itself
        • the heap index, usually initialized as None since it will be
          computed during Dijkstra execution
        • the data contained in the node, actually is the distance
          from the source of the path
        • the predecessor
        • the importance of a node in the graph
    """

    def __init__(self, index, heap_idx, dist, pred, imp=None):
        self.index = index
        self.heap_index = heap_idx
        self.d = dist
        self.pred = pred
        self.importance = imp
    
    def print_node(self):
        if self.pred is not None:
            print(f"index: {self.index}, data: {self.d}, predecessor: {self.pred.index}")
        else:
            print(f"index: {self.index}, data: {self.d}, predecessor: {self.pred}")

class Edge:
    """
    An Edge is simply defined by passing the source, 
    destination node and the weight of the edge itself
    """
    
    def __init__(self, src, dest, weight=1):
        self.u = src
        self.v = dest
        self.weight = weight

class Weighted_Graph:
    """
    A Weighted Graph recieves as inputs a list of vertices and edges. 
    In V we store directly the vertices and then we need to build the
    Adjacency list of the graph itself. Since we are dealing with sparse 
    graphs (remember that we decided to use heaps as priority queues),
    I opted for this solution, otherwise we could have built an Adjacency 
    Matrix and the result would have been equivalent.
    """

    def __init__(self, vertices, edges):
        self.V = vertices
        maximum = max(vertix.index for vertix in vertices)
        self.Adj = [[] for vertix in range(maximum+1)]

        for edge in edges:
            self.Adj[edge.u.index].append((edge.v,edge.weight))
    