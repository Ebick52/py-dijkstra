def dijkstra(graph, source):
    Q= set()                                #set of unvisited vertices
    inf, nan= float('Inf'), float('NaN')    #constant values
    disconnect= []                          #list of unreachable vertices
    dist, prev= [], []                      #return values
    n= len(graph)                           #number of vertices in graph
    for v in range(n):                      #initialize Q, dist and prev
        dist.append(inf)
        prev.append(nan)
        Q.add(v)
    dist[source], prev[source]= 0, nan      #initialize values of source vertex
    while len(Q):                           #loop for finding next connection
        temp= inf                           #minimum distance of Q
        for i in Q:                         #loop for finding vertex with minimum dist
            if dist[i]<=temp:
                u, temp= i, dist[i]
        if temp==inf:                       #for unreachable vertices
            disconnect.append(u)
        Q.remove(u)
        for v in range(n):                  #to calculate new values of dist
            if v!=u and graph[v][u]:
                ctrl= dist[u] + graph[u][v]
                if ctrl < dist[v]:
                    dist[v], prev[v]= ctrl, u
    if disconnect: print('The input graph is disconnected and vertices {} are unreachable from source!'.format(*disconnect))
    return dist, prev


#G= [[0, 7, 9, float('Inf'), float('Inf'), 14], [7, 0, 10, 15, float('Inf'), float('Inf')], [9, 10, 0, 11, float('Inf'), 2], [float('Inf'), 15, 11, 0, 6, float('Inf')], [float('Inf'), float('Inf'), float('Inf'), 6, 0, 9], [14, float('Inf'), 2, float('Inf'), 9, 0]]
G= [[0, 2, float('Inf'), 8], [2, 0, float('Inf'), 3], [float('Inf'), float('Inf'), 0, float('Inf')], [8, 3, float('Inf'), 0]]
print(dijkstra(G, 0))
