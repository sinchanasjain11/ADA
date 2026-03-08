INF = 99999

def dijkstra(graph, source, n):
    visited = [False] * n
    dist = [INF] * n

    dist[source] = 0

    for _ in range(n):
        min_dist = INF
        u = -1

        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        visited[u] = True

        for v in range(n):
            if (not visited[v] and graph[u][v] != INF 
                and dist[u] + graph[u][v] < dist[v]):
                dist[v] = dist[u] + graph[u][v]

    return dist

# Example Graph (Adjacency Matrix)
graph = [
    [0, 4, INF, INF, INF, INF, INF, 8, INF],
    [4, 0, 8, INF, INF, INF, INF, 11, INF],
    [INF, 8, 0, 7, INF, 4, INF, INF, 2],
    [INF, INF, 7, 0, 9, 14, INF, INF, INF],
    [INF, INF, INF, 9, 0, 10, INF, INF, INF],
    [INF, INF, 4, 14, 10, 0, 2, INF, INF],
    [INF, INF, INF, INF, INF, 2, 0, 1, 6],
    [8, 11, INF, INF, INF, INF, 1, 0, 7],
    [INF, INF, 2, INF, INF, INF, 6, 7, 0]
]

source = 0
n = len(graph)

distances = dijkstra(graph, source, n)

print("Vertex\tDistance from Source")
for i in range(n):
    print(i, "\t", distances[i])
