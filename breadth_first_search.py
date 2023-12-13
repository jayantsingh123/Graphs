def breadth_first_search(graph):
    """ Similar to level order traversal, we traverse all neighbors of a node
    before proceeding to next node"""
    L = []
    if len(graph)==0:
        return L
    visited =  [False] * len(graph)
    q = [0]

    visited[0] = True
    while len(q) > 0:
        temp = q.pop(0)
        print(temp)
        L.append(temp)
        if len(graph[temp])>0:
            for j in graph[temp]:
                if visited[j]== False:
                    q.append(j)
                    visited [j] = True
    return L
if __name__ == "__main__":
    res = breadth_first_search([[1,2,5],[0,3],[0,4],[1,5],[2,5],[0,3,4]])