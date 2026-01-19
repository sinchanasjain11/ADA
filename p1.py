class Graph:
    def __init__(self):
        self.edges=[]
        self.vertices=set()
    def add_edge(self,u,v,w):
        self.edges.append((u,v,w))
        self.vertices.add(u)
        self.vertices.add(v)
    def prim_mst(self,start):
        visited=set([start])
        mst=[]
        total_cost=0
        while len(visited)<len(self.vertices):
            min_edge=None
            min_weight=float('inf')
            
            for u,v,w in self.edges:
                if u in visited and v not in visited and w<min_weight:
                    min_weight=w
                    min_edge=(u,v,w)
                elif v in visited and u not in visited and w<min_weight:
                    min_weight=w
                    min_edge=(v,u,w)
            if min_edge is None:
                break
            u,v,w=min_edge
            visited.add(v)
            mst.append((u,v,w))
            total_cost+=w
        print("\nEdges in Minimum cost Spanning tree:")
        for u,v,w in mst:
            print(f"{u}-{v}={w}")
        print("total cost of MST=",total_cost)
g=Graph()
e=int(input("enter number of edges:"))
print("enter edges in format:ab 3")
for _ in range(e):
    edge,weight=input().split()
    u=edge[0]
    v=edge[1]
    w=int(weight)
    g.add_edge(u,v,w)
start_vertex=input("enter starting vertex:")
g.prim_mst(start_vertex)