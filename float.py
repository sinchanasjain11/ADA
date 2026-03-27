# Floyd-Warshall Algorithm for All-Pairs Shortest Paths
INF = float('inf')

def floyd_warshall(graph):
    v = len(graph)
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# Example usage
if __name__ == "__main__":
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]]
    result = floyd_warshall(graph)
    print("Shortest distance matrix:")
    for row in result:
        print(row)