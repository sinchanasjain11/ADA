def topological_sort(n, edges):
    # Adjacency matrix
    adj = [[0]*n for _ in range(n)]
    indegree = [0]*n

    # Build graph
    for u, v in edges:
        adj[u][v] = 1
        indegree[v] += 1

    topo_order = []

    for _ in range(n):
        # Find a source vertex
        source = -1
        for i in range(n):
            if indegree[i] == 0:
                source = i
                break

        # If no source found, cycle exists
        if source == -1:
            print("Topological sorting not possible (Graph has a cycle)")
            return

        topo_order.append(source)
        indegree[source] = -1   # Mark as removed

        # Remove outgoing edges of source
        for j in range(n):
            if adj[source][j] == 1:
                indegree[j] -= 1

    print("Topological Order:")
    print(topo_order)


# -------- Main --------
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    edges.append((u, v))

topological_sort(n, edges)