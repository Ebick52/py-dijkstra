def dijkstra(graph, source):
    Q, inf, nan, disconnect= set(), float('Inf'), float('NaN'), []
    dist, prev, n= [], [], len(graph)
    for v in range(n):
        dist.append(inf)
        prev.append(nan)
        Q.add(v)
    dist[source]= 0
    while len(Q):
        temp= inf
        for i in Q:
            if dist[i]<=temp:
                u, temp= i, dist[i]
        if temp==inf:
            disconnect.append(u)
        Q.remove(u)
        for v in range(n):
            if v!=u and graph[v][u]:
                alt= dist[u] + graph[u][v]
                if alt < dist[v]:
                    dist[v]= alt
                    prev[v]= u
    if disconnect: print('The input graph is disconnected and vertices {} are unreachable from source!'.format(*disconnect))
    return dist, prev


#G= [[0, 7, 9, float('Inf'), float('Inf'), 14], [7, 0, 10, 15, float('Inf'), float('Inf')], [9, 10, 0, 11, float('Inf'), 2], [float('Inf'), 15, 11, 0, 6, float('Inf')], [float('Inf'), float('Inf'), float('Inf'), 6, 0, 9], [14, float('Inf'), 2, float('Inf'), 9, 0]]
G= [[0, 2, float('Inf'), 8], [2, 0, float('Inf'), 3], [float('Inf'), float('Inf'), 0, float('Inf')], [8, 3, float('Inf'), 0]]
print(dijkstra(G, 0))