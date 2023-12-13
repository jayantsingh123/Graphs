class Solution:

    def __init__(self, graph):
        self.graph = graph

    # Function to find a Mother Vertex in the Graph.
    def dfs(self, adj, node, visited):
        visited[node] = True
        for j in adj[node]:
            if not visited[j]:
                self.dfs(adj, j, visited)
        return

    def findMotherVertex(self, V, adj):
        """ mother vertex is the vertex in a Directed graph,
        from where we can access every node"""

        visited = [False] * V
        mother_list = []
        for i in range(V):
            if len(adj[i]) != 0:
                self.dfs(adj, i, visited)
            if sum(visited) == V:
                mother_list.append(i)
            visited = [False] * V
        if len(mother_list) > 0:
            # if there're multiple mother vertices, find the minimum
            return min(mother_list)
        else:
            return -1

if __name__=="__main__":
    obj = Solution([[1],[]])
    res = obj.findMotherVertex(2,[[1],[0]])