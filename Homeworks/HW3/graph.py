class Node:

    def __init__(self, index, heap_idx, dist, pred):
        self.index = index
        self.heap_index = heap_idx
        self.d = dist
        self.pred = pred
    
    def print_node(self):
        print(f"index: {self.index}, data: {self.d}, predecessor: {self.pred}")

class Edge:
    
    def __init__(self, src, dest, weight=1):
        self.u = src
        self.v = dest
        self.weight = weight

class Weighted_Graph:

    def __init__(self, vertices, edges):
        self.V = [vertix for vertix in vertices]
        self.Adj = [[] for vertix in range(len(vertices))]

        for edge in edges:
            self.Adj[edge.u.index].append((edge.v,edge.weight))
    
    def print_adj(self):
        for el in G.V:
            print(el.index)
            for j in el:
                print(f"\t ->{j[0].index}")