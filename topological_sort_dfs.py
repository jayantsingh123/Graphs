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

    def dfs(self, grid, node, visited, st):
        visited[node]=True
        for j in grid[node]:
            if not visited[j]:
                self.dfs(grid, j, visited, st)
        st.append(node)
        return

    def topologicaldfs(self,n,edges):
        """ We use stack(st) to store nodes after recursive call is over.
        e.g. grid = [[1],[],[0,1,3],[],[1]] has st as [1,0,3,2,4]"""
        visited=[False]*n
        grid = self.define_graph(n,edges)
        st,L=[],[]
        for i in range(n):
            if not visited[i]:
                self.dfs(grid, i, visited,st)
        while len(st)>0:
            elem = st.pop()
            L.append(elem)
        return L