class Solution:

    def __init__(self, n, edges):
        self.n = n
        self.edges = edges


    def define_graph (self, n, edges):
        """ given number of nodes and list of directed edges,
          define graph as list of lists """
        grid = [[]for _ in range(n)]
        for i in edges:
            grid[i[0]].append(i[-1])
        return grid

    def indegree(self, n, edges):
        """ define a dictionary which gives for a given key, the number of edges entering it"""

        indegree = {key:0 for key in range(n)}
        for i in edges:
            indegree[i[-1]]+=1
        return indegree


    def topological_sort(self, n, edges):
        indegree = self.indegree(n, edges)
        grid = self.define_graph(n,edges)
        visited = 0
        L=[]
        # implement Kahns BFS
        q = [node for node in indegree.keys() if indegree[node]==0]
        while len(q)>0:
            elem = q.pop(0)
            L.append(elem)
            visited+=1
            if visited==n:
                return L
            for j in grid[elem]:
                indegree[j]-=1
                if indegree[j]==0:
                    q.append(j)
        return "loop detected"

obj = Solution(5, [[0,1],[4,1],[1,4],[2,3]])
result = obj.topological_sort(5, [[0,1],[4,1],[1,4],[2,3]])
