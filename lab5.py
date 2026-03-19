"""Design and implement C/JAVA/Python Program to obtain the Topological ordering 
of vertices in a given digraph.""" 


def topological_sort(n, edges):
    adj = [[0]*n for _ in range(n)]
    indegree = [0]*n

    
    for u, v in edges:
        adj[u][v] = 1
        indegree[v] += 1

    topo_order = []

    for _ in range(n):
        source = -1
        for i in range(n):
            if indegree[i] == 0:
                source = i
                break

        
        if source == -1:
            print("Topological sorting not possible (Graph has a cycle)")
            return

        topo_order.append(source)
        indegree[source] = -1   

        
        for j in range(n):
            if adj[source][j] == 1:
                indegree[j] -= 1

    print("Topological Order:")
    print(topo_order)



n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    edges.append((u, v))

topological_sort(n, edges)
5,4
1 2
1 3
2 4
3 4
