def define_graph(N, edges):
    graph = [[] for _ in range(N)]
    for j in edges:
        graph[j[0]].append(j[-1])
        graph[j[-1]].append(j[0])
    return graph

if __name__ == '__main__':
    res = define_graph(5, [[0, 1], [3,4]])