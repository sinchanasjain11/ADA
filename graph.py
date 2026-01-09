class graph:
    def __init__(self):
        self.edges=[]
        self.vertices=set()
    def add_edge(self,u,v,w):
        self.vertices.add(u)
        self.vertices.add(v)
        
    def find(self ,parent ,i):
        if parent[i] == i:
            return i
        return self.find(parent ,parent[i])
    def union(self ,parent ,rank ,x ,y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
    def kruskal_mst(self):
        self.edges.sort()
        parent = ()
        rank = ()
        for v in self.vertices:
            parent[v] = v
            rank[v] = 0
        mst=[]
        total_cost=0
        for w,u,v in self.edges:
            x=self.find(parent ,u)
            y=self.find(parent ,v)
            if x!=y:
                mst.append((u ,v ,w))
                total_cost+=w
                self.union(parent ,rank ,x ,y)
        print("\n edges in minimum spanning tree")
        for u ,v ,w in mst:
            print(f"{u} -- {v} == {w}")
        print("total cost of mst is :",total_cost)
g=graph()
e=int(input("enter number of edges")) 
print("enter edges in format :ab3")
for _ in range(e):
    edge,weight=input().split()
    u=edge[0]
    v=edge[1]
    w=int(weight)
    g.add_edge(u ,v ,w)
g.kruskal_mst()        