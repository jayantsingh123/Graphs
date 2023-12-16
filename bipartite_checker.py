class Solution:
    """ We check if an undirected graph is bipartite,
    i.e. we can divide the nodes into two distinct groups,
    and every edge connects the nodes from both the groups"""

    def __int__(self):
        pass
    def bfs_help(self, grid):
        n = len(grid)
        visited = [False] * n
        color = [True] * n
        visited[0] = True
        q = [0]
        while len(q)>0:
            elem = q.pop(0)
            for j in grid[elem]:
                if not visited[j]:
                    visited[j] = True
                    color[j] = not color[elem]
                    q.append(j)
                else:
                    if color[j] == color[elem]:
                        return False
        return True

    def bipartite(self, grid):
        return self.bfs_help(grid)
if __name__=="__main__":
    obj = Solution()
    res = obj.bipartite([[1], [0, 2], [1]])

