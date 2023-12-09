def shortest_Path(graph, weight, source):
    """ given a DAG with weighted edges, find the shortest path
    from source to each vertex.
    the output will be  dictionary, with keys being vertices
    and values as distance from source
    Npte that we can't use BFS since, BFS only counts number of edges from source to destination.
    Here we have weights on the edges."""

    q = [source]
    distance = {k: 9999 for k in range(len(graph))}
    distance[source] = 0
    while len(q)>0:
        elem = q.pop(0)
        for j in graph[elem]:
            val = distance[elem] + weight[(elem,j)]
            distance[j] = min(distance[j], val)
            q.append(j)
    return distance


